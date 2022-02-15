import pytest
from ...ethercat.tests.test_device import (
    TestEtherCATDevice as _TestEtherCATDevice,
)
from ...hal.tests.test_device import (
    TestHALDevice as _TestHALDevice,
)
from .base_test_class import BaseLCECTestClass


class TestLCECDevice(BaseLCECTestClass, _TestEtherCATDevice, _TestHALDevice):

    expected_mro = [
        "BogusLCECDevice",
        "LCECSimDevice",
        "LCECDevice",
        *_TestEtherCATDevice.expected_mro[:-5],  # BogusEtherCAT...CiA301
        *_TestHALDevice.expected_mro[1:3],  # HALPinDevice
        *_TestHALDevice.expected_mro[7:],  # BogusDevice...
    ]

    @pytest.fixture
    def obj(self, device_cls, sim_device_data, sdo_data, mock_halcomp):
        self.obj = self.device_model_cls(
            address=sim_device_data["test_address"]
        )
        self.obj.init(comp=mock_halcomp)
        yield self.obj
