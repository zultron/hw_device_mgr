from ...device import CiA402SimDevice
from ....cia_301.tests.bogus_devices.device import (
    BogusCiA301Device,
    BogusCiA301V1Servo,
    BogusCiA301V2Servo,
    BogusCiA301V1IO,
)


class BogusCiA402Device(BogusCiA301Device):
    category = "bogus_cia402_devices"


class BogusCiA402V1Servo(
    BogusCiA402Device, CiA402SimDevice, BogusCiA301V1Servo
):
    name = "bogo_cia402_v1_servo"
    product_code = 0xB0905020


class BogusCiA402V2Servo(
    BogusCiA402Device, CiA402SimDevice, BogusCiA301V2Servo
):
    name = "bogo_cia402_v2_servo"
    product_code = 0xB0905021


class BogusCiA402V1IO(BogusCiA402Device, BogusCiA301V1IO):
    name = "bogo_cia402_v1_io"
    product_code = 0xB0901020
