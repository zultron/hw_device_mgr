from ..mgr_hal.mgr import HALHWDeviceMgr, SimHALHWDeviceMgr
from ..mgr_ros.mgr import ROSHWDeviceMgr, SimROSHWDeviceMgr
from .devices import ManagedDevices, SimManagedEtherCATDevices


class ROSHALHWDeviceMgr(ROSHWDeviceMgr, HALHWDeviceMgr):
    data_type_class = ManagedDevices.data_type_class
    device_base_class = ManagedDevices
    device_classes = ManagedDevices.get_model()


class SimROSHALHWDeviceMgr(
    SimROSHWDeviceMgr, SimHALHWDeviceMgr
):

    device_base_class = SimManagedEtherCATDevices
    device_classes = SimManagedEtherCATDevices.get_model()
