import pytest
from ...tests.base_test_class import BaseTestClass
from ..data_types import CiA301DataType
from ..sdo import CiA301SDO
from ..config import CiA301SimConfig
from .bogus_devices.device import (
    BogusCiA301Device,
    BogusCiA301V1Servo,
    BogusCiA301V2Servo,
    BogusCiA301V1IO,
)
from ..command import CiA301SimCommand


class BaseCiA301TestClass(BaseTestClass):
    """Base test class for CiA301 module."""

    #
    # Configuration for test subclasses
    #

    # The device configuration, as in a real system
    device_config_yaml = "cia_301/tests/device_config.yaml"

    # Device model SDOs; for test fixture
    device_sdos_yaml = "cia_301/tests/bogus_devices/sim_sdo_data.yaml"

    # Classes under test in this module
    data_type_class = CiA301DataType
    sdo_class = CiA301SDO
    command_class = CiA301SimCommand
    config_class = CiA301SimConfig
    device_class = BogusCiA301Device
    device_model_classes = (
        BogusCiA301V1Servo,
        BogusCiA301V2Servo,
        BogusCiA301V1IO,
    )
    device_model_sdo_clone = None
    load_device_sdos_yaml = True  # EtherCAT classes get SDO data from ESI file

    def init_sim(self):
        if self.load_device_sdos_yaml:
            # Sim device & SDO data
            path, sdo_data = self.load_yaml(self.device_sdos_yaml, True)
            sdo_data = self.munge_sdo_data(sdo_data)
            super().init_sim(sdo_data=sdo_data)
        else:
            super().init_sim()
        # Device config
        self.init_device_config()

    def init_device_config(self):
        # Device config
        self.config_class._device_config.clear()
        path, dev_conf = self.load_yaml(self.device_config_yaml, True)
        dev_conf = self.munge_device_config(device_config=dev_conf)
        self.device_class.set_device_config(dev_conf)

    @classmethod
    def munge_device_config(cls, *, device_config):
        new_device_config = list()
        for conf in device_config:
            if cls.irrelevant_test_category(conf["test_category"]):
                continue  # Skip irrelevant data
            device_cls = cls.test_category_class(conf["test_category"])
            assert device_cls
            new_device_config.append(conf)
            conf["vendor_id"], conf["product_code"] = device_cls.device_model_id()
        assert new_device_config  # Sanity check not empty
        return new_device_config

    @pytest.fixture
    def extra_fixtures(self):
        # Use this to add extra fixtures to the `device_cls` fixture
        # in subclasses
        pass

    @pytest.fixture
    def device_cls(self, extra_fixtures):
        self.init_sim()
        yield self.device_class

    @pytest.fixture
    def config_cls(self, device_cls):
        yield self.config_class

    @pytest.fixture
    def command_cls(self, device_cls):
        yield self.command_class

    @pytest.fixture
    def device_config(self, device_cls, request):
        """
        Device configuration data fixture.

        Load device configuration from file named in
        `device_config_yaml` attr.

        Device configuration in the same format as non-test
        configuration, described in `Config` classes.

        The absolute path is stored in the test object
        `device_config_path` attribute.

        Optionally, to make the YAML file reusable, each
        configuration's `vendor_id` and `product_code` keys may be
        replaced with a `category` key matching a parent of classes
        listed; this fixture will re-add those keys.
        """
        request.instance.device_config = self.config_class._device_config
        yield request.instance.device_config

    @pytest.fixture
    def all_device_data(self, device_cls, request):
        """
        Device data from file named in `sim_device_data_yaml` attr.

        Device data is reformatted for ease of use in a `list` of `dict`:
        `model_key`:   `bogus_devices.device` model class attribute
        `bus`, `position`:  Device address
        `params`:  `dict` of SDO initial values
          `(idx, subidx)`:  Initial value, `DataType` instance

        The same data is available in the test object `dev_data` as a
        `dict` with device address key `(bus, position)`.
        """
        request.instance.sim_device_data = self.command_class.sim_device_data
        yield request.instance.sim_device_data

    @pytest.fixture
    def all_sdo_data(self, device_cls, request):
        """
        SDO data from file named in `device_sdos_yaml` attr.

        SDO data is read from file and reformatted for ease of use in
        a `dict`:

        `model_key`:  # `bogus_devices.device` model class attribute
          `(idx, subidx)`:  # One key (`tuple` of `int`) for each SDO of device
            `index`:  # SDO index
            `subindex`:  # ...and subindex
            `address`:  # `tuple(index, subindex)`
            `data_type`:  # `DataType` subclass
            `name`:  # Human-readable name
            `index_name`:  # Optional, human-readable category, default `""`
            `pdo_mapping`:  # If PDO mappable, `R` or `T`, else `None`
            `ro`:  # `True` or `False`
            `default_value`:  # Default value, `DataType` instance, default `0`
        """
        request.instance.sdo_data = self.command_class.sim_sdo_data
        request.instance.sdo_values = self.command_class.sim_sdo_values
        yield request.instance.sdo_data

    #
    # Dynamic test parameterization
    #

    @pytest.fixture
    def sim_device_data(self, _sim_device_data, device_cls):
        """
        Parametrize test with values from `all_device_data` fixture.

        When combined with the `sdo_data` fixture, `sim_device_data`
        values will match that fixture's device model.

        The `sim_device_data` is also available in the test instance's
        `sim_device_data` attribute.
        """
        self.sim_device_data = _sim_device_data
        model_id = _sim_device_data["vendor_id"], _sim_device_data["product_code"]
        _sim_device_data["test_model_id"] = model_id
        self.device_model_cls = device_cls.get_model(model_id)
        assert self.device_model_cls
        yield _sim_device_data

    @pytest.fixture
    def sdo_data(self, _sdo_data, device_cls):
        """
        Parametrize test with values from `all_sdo_data` fixture.

        When combined with the `sim_device_data` fixture, `sdo_data`
        values will match that fixture's device model.

        The `sdo_data` is also available in the test instance's
        `sdo_data` attribute.
        """
        self.sdo_data = _sdo_data
        yield _sdo_data

    @classmethod
    def munge_sdo_data(cls, sdo_data, conv_sdos=False):
        new_sdo_data = dict()
        for test_category, old_sdos in sdo_data.items():
            if cls.irrelevant_test_category(test_category):
                continue  # Skip irrelevant data
            device_cls = cls.test_category_class(test_category)
            assert device_cls
            sdos = new_sdo_data[device_cls.name] = dict()
            for ix, sdo in old_sdos.items():
                if conv_sdos:
                    ix = cls.config_class.sdo_ix(ix)
                    sdos[ix] = cls.sdo_class(**sdo)
                else:
                    sdos[ix] = sdo
        assert new_sdo_data
        assert None not in new_sdo_data.keys()
        return new_sdo_data

    @classmethod
    def munge_sim_device_data(cls, sim_device_data):
        sim_device_data = super().munge_sim_device_data(sim_device_data)
        # Hack support for the HWDeviceMgr class
        device_base_cls = getattr(cls, "device_base_class", cls.device_class)
        for dev in sim_device_data:
            # Get device class from test_category key
            device_cls = cls.test_category_class(dev["test_category"])
            # Replace model_id key
            dev.pop("model_id")
            dev["vendor_id"], dev["product_code"] = device_cls.device_model_id()
            # For test fixture
            dev["test_address"] = (dev["bus"], dev["position"])
        return sim_device_data

    def pytest_generate_tests(self, metafunc):
        # Dynamic parametrization from sim_device_data_yaml:
        # - _sim_device_data:  iterate through `sim_device_data` list
        #   - with `_sdo_data`:  add matching entry in `sdo_data` list
        # - _sdo_data:  iterate through `sdo_data` values
        # - bus:  iterate through `sim_device_data` unique `bus` values
        # *Note all three cases are mutually exclusive
        path, dev_data = self.load_yaml(self.sim_device_data_yaml, True)
        dev_data = self.munge_sim_device_data(dev_data)
        path, sdo_data = self.load_yaml(self.device_sdos_yaml, True)
        sdo_data = self.munge_sdo_data(sdo_data, conv_sdos=True)
        names = list()
        vals, ids = (list(), list())
        if "_sim_device_data" in metafunc.fixturenames:
            names.append("_sim_device_data")
            assert "bus" not in metafunc.fixturenames  # use sim_device_data["bus"]
            if "_sdo_data" in metafunc.fixturenames:
                names.append("_sdo_data")
            for dev in dev_data:
                ids.append(f"{dev['test_name']}@{dev['test_address']}")
                if "_sdo_data" in metafunc.fixturenames:
                    device_cls = self.test_category_class(dev["test_category"])
                    assert device_cls is not None
                    vals.append([dev, sdo_data[device_cls.name]])
                else:
                    vals.append(dev)
        elif "_sdo_data" in metafunc.fixturenames:
            names.append("_sdo_data")
            for category, device_sdos in sdo_data.items():
                vals.append(device_sdos)
                ids.append(category)
        elif "bus" in metafunc.fixturenames:
            names.append("bus")
            vals = list(d for d in {d["bus"] for d in dev_data})
            ids.extend(f"bus{b}" for b in vals)
        if names:
            metafunc.parametrize(",".join(names), vals, ids=ids, scope="class")
