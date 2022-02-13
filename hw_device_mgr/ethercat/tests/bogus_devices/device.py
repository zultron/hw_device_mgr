from ...device import EtherCATSimDevice
from ....cia_402.tests.bogus_devices.device import (
    BogusCiA402Device, BogusCiA402V1Servo, BogusCiA402V2Servo, BogusCiA402V1IO
)


class BogusEtherCATDevice(EtherCATSimDevice, BogusCiA402Device):
    category = "bogus_ethercat_devices"

    @classmethod
    def set_device_xml_dir(cls, path):
        # Tests generate customized ESI file in temp directory; provide a hook
        # to point fixtures to it
        cls.xml_base_dir = path

    @classmethod
    def xml_description_path(cls):
        if not hasattr(cls, "xml_base_dir"):
            return super().xml_description_path()
        return cls.xml_base_dir / cls.device_xml_dir / cls.xml_description_fname

    @classmethod
    def orig_xml_description_path(cls):
        return super().xml_description_path()


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
