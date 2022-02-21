from ...mgr import SimROSHALHWDeviceMgr
from ....mgr_hal.tests.bogus_devices.mgr import HALHWDeviceMgrTest


class ROSHWDeviceMgrTestCategory(SimROSHALHWDeviceMgr):
    category = "test_ros_hal_hw_device_mgr"
    device_base_class = HALHWDeviceMgrTest.device_base_class
    device_classes = HALHWDeviceMgrTest.device_classes

class ROSHWDeviceMgrTest(ROSHWDeviceMgrTestCategory):
    name = "test_ros_hal_hw_device_mgr"
