from ...device import HALPinDevice
from ....cia_402.tests.bogus_devices.device import (
    BogusCiA402Device, BogusCiA402V1Servo, BogusCiA402V2Servo, BogusCiA402V1IO
)


class BogusHALDevice(HALPinDevice, BogusCiA402Device):
    category = "bogus_hal_device"
    vendor_id = 0xB090C0


class BogusHALV1Servo(BogusHALDevice, BogusCiA402V1Servo):
    name = "bogo_hal_v1_servo"
    product_code = 0xB0905050


class BogusHALV2Servo(BogusHALDevice, BogusCiA402V2Servo):
    name = "bogo_hal_v2_servo"
    product_code = 0xB0905051


class BogusHALV1IO(BogusHALDevice, BogusCiA402V1IO):
    name = "bogo_hal_v1_io"
    product_code = 0xB0901050
