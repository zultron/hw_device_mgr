from ..mgr_hal.mgr import HALHWDeviceMgr, SimHALHWDeviceMgr
from ..mgr_ros.mgr import ROSHWDeviceMgr, SimROSHWDeviceMgr
from .devices import ManagedDevices, SimManagedLCECDevices


class ROSHALHWDeviceMgr(ROSHWDeviceMgr, HALHWDeviceMgr):
    name = "ros_hal_hw_device_mgr"
    data_type_class = ManagedDevices.data_type_class
    device_base_class = ManagedDevices
    device_classes = ManagedDevices.get_model()


class SimROSHALHWDeviceMgr(ROSHALHWDeviceMgr, SimROSHWDeviceMgr, SimHALHWDeviceMgr):

    name = "sim_ros_lcec_hw_device_mgr"
    device_base_class = SimManagedLCECDevices
    device_classes = SimManagedLCECDevices.get_model()
