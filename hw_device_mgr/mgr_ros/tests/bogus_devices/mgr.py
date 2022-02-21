from ...mgr import SimROSHWDeviceMgr
from ....mgr.tests.bogus_devices.mgr import (
    HwMgrTestDevices,
    HwMgrTestElmoGold420,
    HwMgrTestElmoGold520,
    HwMgrTestInovanceIS620N,
    HwMgrTestInovanceSV660N,
)


class ROSHWDeviceMgrTestCategory(SimROSHWDeviceMgr):
    category = "test_ros_hw_device_mgr"
    device_base_class = HwMgrTestDevices
    device_classes = (
        HwMgrTestElmoGold420,
        HwMgrTestElmoGold520,
        HwMgrTestInovanceIS620N,
        HwMgrTestInovanceSV660N,
    )

class ROSHWDeviceMgrTest(ROSHWDeviceMgrTestCategory):
    name = "test_ros_hw_device_mgr"
