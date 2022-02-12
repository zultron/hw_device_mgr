from ...device import EtherCATSimDevice
from ....cia_402.tests.bogus_devices.device import (
    BogusCiA402Device, BogusCiA402V1Servo, BogusCiA402V2Servo, BogusCiA402V1IO
)


class BogusEtherCATDevice(EtherCATSimDevice, BogusCiA402Device):
    category = "bogus_ethercat_devices"


class BogusEtherCATServo(BogusEtherCATDevice, BogusCiA402V1Servo):
    name = "bogo_ethercat_servo"
    product_code = 0xB0905030
    xml_description_fname = "BogusServo.xml"


class BogusOtherCATServo(BogusEtherCATDevice, BogusCiA402V2Servo):
    name = "bogo_Othercat_servo"
    product_code = 0xB0905031
    xml_description_fname = "BogusServo.xml"


class BogusEtherCATIO(BogusEtherCATDevice, BogusCiA402V1IO):
    name = "bogo_ethercat_io"
    product_code = 0xB0901030
    xml_description_fname = "BogusIO.xml"
