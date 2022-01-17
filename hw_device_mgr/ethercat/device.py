import abc
from ..cia_301.device import CiA301Device, CiA301SimDevice
from .config import EtherCATConfig, EtherCATSimConfig
from .data_types import EtherCATDataType


class EtherCATDevice(CiA301Device, abc.ABC):
    """
    Abstract class representing an EtherCAT CoE device.

    Device instances are addressed by `(master, position)`.

    Device model subclasses have matching XML description, methods
    (e.g. set params volatile) and other features specific to that
    model.
    """

    category = "EtherCAT"

    # Resource names for locating device description XML and error files
    device_xml_dir = "device_xml"

    # Filename of XML description
    xml_description_fname = None

    # Swappable utility classes
    data_type_class = EtherCATDataType
    config_class = EtherCATConfig

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_device_sdos_from_esi()

    @property
    def master(self):
        return self.address[0]

    @property
    def position(self):
        return self.address[1]

    @abc.abstractmethod
    def set_params_volatile(self, nv=False):
        """
        Set device params volatile or non-volatile.

        Concrete subclasses may optionally implement this
        """

    @classmethod
    def xml_description_path(cls):
        """
        Return path to device ESI file.

        Path is under the module directory,
        `{device_xml_dir}/{xml_description_fname}`.
        """
        # print("cls:", cls)
        # print("cls.device_xml_dir", cls.device_xml_dir)
        # print("cls.xml_description_fname", cls.xml_description_fname)
        # print("cls.pkg_path()", cls.pkg_path("."))
        return cls.pkg_path(cls.device_xml_dir) / cls.xml_description_fname

    @classmethod
    def add_device_sdos_from_esi(cls):
        """Read device SDOs from ESI file and add to configuration."""
        # print("EtherCATDevice:  add_device_sdos_from_esi")
        sdo_data = dict()
        dev_esi_paths = set()
        for dev in cls.get_model():
            # model_id = dev.device_type_key()
            esi_path = dev.xml_description_path()
            if esi_path in dev_esi_paths:
                # print(f"Skipping duplicate ESI {esi_path}")
                # assert model_id in sdo_data
                continue
            dev_esi_paths.add(esi_path)
            dev_sdo_data = dev.config_class.get_device_sdos_from_esi(esi_path)
            # print(f"Reading ESI {esi_path} for model_id {model_id}")
            # print("dev_sdo_data.keys():", list(dev_sdo_data.keys()))
            # print("dev_sdo_data:", dev_sdo_data)
            sdo_data.update(dev_sdo_data)
            # assert model_id in sdo_data
            # print(
            #     "add_device_sdos_from_esi model_id",
            #     model_id,
            #     "sdo_data.keys()",
            #     sdo_data.keys(),
            # )
            # print(
            #     "add_device_sdos_from_esi sdo_data[model_id].keys()",
            #     sdo_data[model_id].keys(),
            # )
        cls.add_device_sdos(sdo_data)


class EtherCATSimDevice(EtherCATDevice, CiA301SimDevice):
    config_class = EtherCATSimConfig

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params_volatile = False

    def set_params_volatile(self, nv=False):
        self.params_volatile = not nv

    @classmethod
    def munge_sdo_data(cls, sdo_data):
        # print("ethercat munge_sdo_data cls:", cls)
        res = dict()
        for model_id, sdos in sdo_data.items():
            model_sdos = res[model_id] = dict()
            for ix, sdo in sdos.items():
                model_sdos[ix] = sdo
        # print("ethercat munge_sdo_data res:", res)
        return res

    @classmethod
    def init_sim(cls, device_data=dict()):
        """
        Configure device, config, command for sim EtherCAT devices.

        Like parent `CiA301SimDevice.init_sim()`, but parse SDO data
        from EtherCAT ESI description file and pass with sim device data
        to parent class's method.
        """
        # print("EtherCATSimDevice:  init_sim")
        cls.add_device_sdos_from_esi()
        # print("EtherCATSimDevice device_data", device_data)
        device_data = cls.munge_device_data(device_data)
        # print(f"CiA301SimDevice init_sim device_data:", device_data)
        cls.config_class.init_sim(device_data=device_data)

    @classmethod
    def add_device_sdos(cls, sdo_data):
        """
        Add SDO data to all known devices.

        So that test ESI files are reusable and don't need to be
        duplicated just to change the device product code, go through
        devices and any missing SDO data, add that from a similar
        device.
        """

        # print("EtherCATSimDevice:  add_device_sdos")
        # print("sdo_data.keys() before", list(sdo_data.keys()))
        for model_cls in cls.get_model():
            # print(
            #    f"Looking for model {model_cls}, {model_cls.device_type_key()}"
            # )
            for device_cls in model_cls.__mro__:
                if "product_code" not in device_cls.__dict__:
                    # print(f"  skipping {device_cls}:  no product_code")
                    continue
                model_id = device_cls.device_type_key()
                # print("  device_cls + model_id", device_cls, model_id)
                if model_id in sdo_data:
                    sdo_data[model_cls.device_type_key()] = sdo_data[model_id]
                    # print("      got it:", model_id)
                    break
            # else:
            #     print("      don't got it")
        # print("sdo_data keys after", repr(sdo_data.keys()))
        # print("ethercat device add_device_sdos sdo_data after", sdo_data)
        super().add_device_sdos(sdo_data)
