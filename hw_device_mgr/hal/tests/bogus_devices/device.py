from ...device import HALPinDevice
from ....cia_301.tests.bogus_devices.device import (
    BogusCiA301DeviceCategory,
    BogusCiA301V1ServoCategory,
    BogusCiA301V2ServoCategory,
    BogusCiA301V1IOCategory,
)


class BogusHALDevice(HALPinDevice, BogusCiA301DeviceCategory):
    category = "bogus_hal_device"
    vendor_id = 0xB090C0


class BogusHALV1Servo(BogusHALDevice, BogusCiA301V1ServoCategory):
    name = "bogo_hal_v1_servo"
    product_code = 0xB0905050


class BogusHALV2Servo(BogusHALDevice, BogusCiA301V2ServoCategory):
    name = "bogo_hal_v2_servo"
    product_code = 0xB0905051


class BogusHALV1IO(BogusHALDevice, BogusCiA301V1IOCategory):
    name = "bogo_hal_v1_io"
    product_code = 0xB0901050
