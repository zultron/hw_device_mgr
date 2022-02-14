from ...mgr_hal.tests.base_test_class import BaseHALMgrTestClass
from ...mgr_ros.tests.base_test_class import BaseROSMgrTestClass
from .bogus_devices.mgr import ROSHWDeviceMgrForTest
# from ...devices.tests.test_devices_402 import Test402Devices as _Test402Devices
import pytest


###############################
# Test class


class BaseROSHALMgrTestClass(BaseROSMgrTestClass, BaseHALMgrTestClass):
    """Base test class for `ROSHALHWDeviceMgr` class."""

    data_type_class = ROSHWDeviceMgrForTest.data_type_class
    device_class = ROSHWDeviceMgrForTest
    device_base_class = ROSHWDeviceMgrForTest.device_base_class
    device_model_classes = ROSHWDeviceMgrForTest.device_classes

    @pytest.fixture
    def extra_fixtures(
        self,
        manager_ros_params, sim_device_data_path, device_config_path,
        mock_hal, mock_ethercat_command
    ):
        pass
