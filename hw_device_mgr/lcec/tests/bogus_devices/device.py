from ...device import LCECSimDevice
from ....ethercat.tests.bogus_devices.device import (
    BogusEtherCATDevice, BogusEtherCATServo, BogusOtherCATServo, BogusEtherCATIO
)


class BogusLCECDevice(LCECSimDevice, BogusEtherCATDevice):
    category = "bogus_lcec_devices"


class BogusLCECV1Servo(BogusLCECDevice, BogusEtherCATServo):
    name = "bogo_lcec_v1_servo"
    product_code = 0xB0905060
    xml_description_fname = "BogusServo.xml"


class BogusLCECV2Servo(BogusLCECDevice, BogusOtherCATServo):
    name = "bogo_lcec_v2_servo"
    product_code = 0xB0905061
    xml_description_fname = "BogusServo.xml"


class BogusLCECV1IO(BogusLCECDevice, BogusEtherCATIO):
    name = "bogo_lcec_v1_io"
    product_code = 0xB0901060
    xml_description_fname = "BogusIO.xml"
