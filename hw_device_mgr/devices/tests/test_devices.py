from .base_test_class import BaseDevicesTestClass
from ...lcec.tests.test_device import TestLCECDevice as _TestLCECDevice


class TestDevices(BaseDevicesTestClass, _TestLCECDevice):
    expected_mro = [
        "DevicesForTest",
        *[n for n in _TestLCECDevice.expected_mro if not n.startswith("Bogus")],
    ]
