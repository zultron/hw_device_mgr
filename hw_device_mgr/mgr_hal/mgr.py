from ..mgr.mgr import HWDeviceMgr, SimHWDeviceMgr
from ..hal.device import HALCompDevice, HALPinDevice, SimHALPinDevice


class HALHWDeviceMgr(HWDeviceMgr, HALCompDevice, HALPinDevice):
    """Hardware device manager with HAL pins."""

    hal_comp_name = "hw_device_mgr"
    data_type_class = HALPinDevice.data_type_class
    device_base_class = HALPinDevice

    def init_devices(self, **kwargs):
        super().init_devices(**kwargs)
        self.hal_comp_ready()

    def init_device_instances(self, **kwargs):
        super().init_device_instances(comp=self.comp, **kwargs)


class SimHALHWDeviceMgr(HALHWDeviceMgr, SimHWDeviceMgr, SimHALPinDevice):
    """Hardware device manager with HAL pins."""
    device_base_class = SimHALPinDevice
