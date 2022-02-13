# Test and test Device base classes
from ...lcec.tests.test_device import TestLCECDevice as _TestLCECDevice
from ...lcec.device import LCECSimDevice
from ...cia_402.device import CiA402SimDevice

# Device model classes
from ..elmo_gold import ElmoGold420, ElmoGold520
from ..inovance_is620n import InovanceIS620N
from ..inovance_sv660 import InovanceSV660


class DevicesForTest(LCECSimDevice):
    category = "devices_for_test"


class ElmoGold420ForTest(DevicesForTest, ElmoGold420):
    name = "elmo_gold_0x30924_0x10420_test"
    test_category = "elmo_gold_420_test"


class ElmoGold520ForTest(DevicesForTest, ElmoGold520):
    name = "elmo_gold_0x30925_0x10420_test"
    test_category = "elmo_gold_520_test"


class InovanceIS620NForTest(DevicesForTest, InovanceIS620N):
    name = "IS620N_ECAT_test"
    test_category = "inovance_sv660n_test"


class InovanceSV660NForTest(DevicesForTest, InovanceSV660):
    name = "SV660_ECAT_test"
    test_category = "inovance_is620n_test"


class TestDevices(_TestLCECDevice):
    expected_mro = [
        "DevicesForTest",
        *[n for n in _TestLCECDevice.expected_mro if not n.startswith("Bogus")],
    ]

    device_class = DevicesForTest
    # device_class = DevicesForTest
    device_model_classes = (
        ElmoGold420ForTest,
        ElmoGold520ForTest,
        InovanceIS620NForTest,
        InovanceSV660NForTest,
    )
    device_model_sdo_clone = None

    device_config_yaml = "devices/tests/device_config.yaml"
    sim_device_data_yaml = "devices/tests/sim_devices.yaml"
    device_sdos_yaml = "devices/tests/sim_sdo_data.yaml"
