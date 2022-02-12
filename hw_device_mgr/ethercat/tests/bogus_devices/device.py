from ...device import EtherCATSimDevice
from ....cia_301.tests.bogus_devices.device import (
    BogusCiA301DeviceCategory,
    BogusCiA301V1ServoCategory,
    BogusV2CiA301ServoCategory,
    BogusCiA301V1IOCategory,
)


class BogusEtherCATDevice(EtherCATSimDevice, BogusCiA301DeviceCategory):
    category = "bogus_ethercat_devices"


class BogusEtherCATServo(BogusEtherCATDevice, BogusCiA301V1ServoCategory):
    name = "bogo_ethercat_servo"
    product_code = 0xB0905030
    xml_description_fname = "BogusServo.xml"


class BogusOtherCATServo(BogusEtherCATDevice, BogusV2CiA301ServoCategory):
    name = "bogo_Othercat_servo"
    product_code = 0xB0905031
    xml_description_fname = "BogusServo.xml"


class BogusEtherCATIO(BogusEtherCATDevice, BogusCiA301V1IOCategory):
    name = "bogo_ethercat_io"
    product_code = 0xB0901030
    xml_description_fname = "BogusIO.xml"
