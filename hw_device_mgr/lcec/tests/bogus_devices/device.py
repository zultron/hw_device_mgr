from ...device import LCECSimDevice
from ....cia_301.tests.bogus_devices.device import (
    BogusCiA301DeviceCategory,
    BogusCiA301V1ServoCategory,
    BogusCiA301V2ServoCategory,
    BogusCiA301V1IOCategory,
)


class BogusLCECDevice(LCECSimDevice, BogusCiA301DeviceCategory):
    category = "bogus_lcec_devices"


class BogusLCECV1Servo(BogusLCECDevice, BogusCiA301V1ServoCategory):
    name = "bogo_lcec_v1_servo"
    product_code = 0xB0905060
    xml_description_fname = "BogusServo.xml"


class BogusLCECV2Servo(BogusLCECDevice, BogusCiA301V2ServoCategory):
    name = "bogo_lcec_v2_servo"
    product_code = 0xB0905061
    xml_description_fname = "BogusServo.xml"


class BogusLCECV1IO(BogusLCECDevice, BogusCiA301V1IOCategory):
    name = "bogo_lcec_v1_io"
    product_code = 0xB0901060
    xml_description_fname = "BogusIO.xml"
