from ...tests.test_device import TestDot
from .base_test_class import BaseROSHALMgrTestClass
from ...mgr_ros.tests.test_mgr import TestROSHWDeviceMgr as _TestROSHWDeviceMgr
from ...mgr_hal.tests.test_mgr import TestHALHWDeviceMgr as _TestHALHWDeviceMgr


class TestROSHWDeviceMgr(
    BaseROSHALMgrTestClass, _TestROSHWDeviceMgr, _TestHALHWDeviceMgr
):

    expected_mro = [
        "ROSHWDeviceMgrForTest",
        "SimROSHALHWDeviceMgr",
        "ROSHALHWDeviceMgr",
        *_TestROSHWDeviceMgr.expected_mro[1:3],
        *_TestHALHWDeviceMgr.expected_mro[1:],
    ]
