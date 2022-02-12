from ...device import EtherCATSimDevice
from ....cia_301.tests.bogus_devices.device import (
    BogusCiA301Device, BogusCiA301V1Servo, BogusCiA301V2Servo, BogusCiA301V1IO
)


class BogusEtherCATDevice(EtherCATSimDevice, BogusCiA301Device):
    category = "bogus_ethercat_devices"


class BogusEtherCATServo(BogusEtherCATDevice, BogusCiA301V1Servo):
    name = "bogo_ethercat_servo"
    product_code = 0xB0905030
    xml_description_fname = "BogusServo.xml"


class BogusOtherCATServo(BogusEtherCATDevice, BogusCiA301V2Servo):
    name = "bogo_Othercat_servo"
    product_code = 0xB0905031
    xml_description_fname = "BogusServo.xml"


class BogusEtherCATIO(BogusEtherCATDevice, BogusCiA301V1IO):
    name = "bogo_ethercat_io"
    product_code = 0xB0901030
    xml_description_fname = "BogusIO.xml"
