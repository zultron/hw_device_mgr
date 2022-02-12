from ...mgr import SimHALHWDeviceMgr
from ....mgr.tests.bogus_devices.mgr import BogusHWDeviceMgr
from ....lcec.tests.bogus_devices.device_402 import (
    BogusLCEC402Device,
    BogusLCEC402V1Servo,
    BogusV2LCEC402Servo,
)


class BogusLCEC402HWDeviceMgr(SimHALHWDeviceMgr, BogusHWDeviceMgr):
    data_type_class = BogusLCEC402Device.data_type_class
    device_base_class = BogusLCEC402Device
    device_classes = (BogusLCEC402V1Servo, BogusV2LCEC402Servo)

    name = "bogus_lcec_hw_device_mgr"
