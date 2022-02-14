from ...mgr import SimROSHALHWDeviceMgr
from ....mgr_hal.tests.bogus_devices.mgr import HALHWDeviceMgrForTest

class ROSHWDeviceMgrForTest(SimROSHALHWDeviceMgr):
    device_base_class = HALHWDeviceMgrForTest.device_base_class
    device_classes = HALHWDeviceMgrForTest.device_classes
    name = "ros_hal_hw_device_mgr_for_test"
