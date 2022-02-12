from ...device import LCECSimDevice
from ....cia_402.tests.bogus_devices.device import (
    BogusCiA402DeviceCategory,
    BogusCiA402V1ServoCategory,
    BogusCiA402V2ServoCategory,
)


class BogusLCEC402Device(LCECSimDevice, BogusCiA402DeviceCategory):
    category = "bogus_lcec_402_devices"
    xml_description_fname = "BogusServo.xml"
    vendor_id = 0xB090C0


class BogusLCEC402V1Servo(BogusLCEC402Device, BogusCiA402V1ServoCategory):
    name = "bogo_lcec_402_v1_servo"
    product_code = 0xB0905062


class BogusLCEC402V2Servo(BogusLCEC402Device, BogusCiA402V2ServoCategory):
    name = "bogo_lcec_402_v2_servo"
    product_code = 0xB0905063
