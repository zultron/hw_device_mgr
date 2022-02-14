from ...mgr.tests.base_test_class import BaseMgrTestClass
from ...lcec.tests.base_test_class import BaseLCECTestClass
from .bogus_devices.mgr import HALHWDeviceMgrForTest
import pytest


class BaseHALMgrTestClass(BaseMgrTestClass, BaseLCECTestClass):
    """Base test class for `HALHWDeviceMgr` class."""

    # Manager class
    device_class = HALHWDeviceMgrForTest

    # Data types
    data_type_class = HALHWDeviceMgrForTest.data_type_class

    # Base class for attached devices
    device_base_class = HALHWDeviceMgrForTest.device_base_class

    # Attached device classes
    device_model_classes = HALHWDeviceMgrForTest.device_classes

    @pytest.fixture
    def extra_fixtures(self, mock_hal, mock_ethercat_command):
        pass
