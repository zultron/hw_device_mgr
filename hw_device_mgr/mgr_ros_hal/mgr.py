from ..mgr_hal.mgr import HALHWDeviceMgr
from ..mgr_ros.mgr import ROSHWDeviceMgr
from ..mgr.mgr import SimHWDeviceMgr
from .devices import (
    ManagedDevices,
    SimManagedLCECDevices,
    SimManagedEtherCATDevices,
)


class ROSHALHWDeviceMgr(ROSHWDeviceMgr, HALHWDeviceMgr):

    data_type_class = ManagedDevices.data_type_class
    device_base_class = ManagedDevices
    device_classes = ManagedDevices.get_model()


class SimROSLCECHWDeviceMgr(ROSHALHWDeviceMgr, SimHWDeviceMgr):

    device_base_class = SimManagedLCECDevices
    device_classes = SimManagedLCECDevices.get_model()


class SimROSEtherCATHWDeviceMgr(ROSHALHWDeviceMgr, SimHWDeviceMgr):

    device_base_class = SimManagedEtherCATDevices
    device_classes = SimManagedEtherCATDevices.get_model()
