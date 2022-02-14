from ...mgr import SimROSHWDeviceMgr
from ....mgr.tests.bogus_devices.mgr import (
    HWDeviceMgrForTest,
    HwMgrTestDevices,
    HwMgrTestElmoGold420, HwMgrTestElmoGold520,
    HwMgrTestInovanceIS620N,
    HwMgrTestInovanceSV660N,
)


class ROSHWDeviceMgrForTest(SimROSHWDeviceMgr):
    device_base_class = HwMgrTestDevices
    device_classes = (
        HwMgrTestElmoGold420,
        HwMgrTestElmoGold520,
        HwMgrTestInovanceIS620N,
        HwMgrTestInovanceSV660N,
    )

    name = "ros_hw_device_mgr_for_test"
