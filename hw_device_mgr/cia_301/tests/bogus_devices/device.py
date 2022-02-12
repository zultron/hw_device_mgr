from ...device import CiA301SimDevice
from ....tests.bogus_devices.device import (
    BogusDevice,
    BogusV1Servo,
    BogusV2Servo,
    BogusV1IO,
)


class BogusCiA301Device(CiA301SimDevice, BogusDevice):
    category = "bogus_cia301_devices"
    vendor_id = 0xB090C0


class BogusV1CiA301Servo(BogusCiA301Device, BogusV1Servo):
    name = "bogo_cia301_v1_servo"
    product_code = 0xB0905010


class BogusV2CiA301Servo(BogusCiA301Device, BogusV2Servo):
    name = "bogo_cia301_v2_servo"
    product_code = 0xB0905011


class BogusV1CiA301IO(BogusCiA301Device, BogusV1IO):
    name = "bogo_cia301_v1_io"
    product_code = 0xB0901010
