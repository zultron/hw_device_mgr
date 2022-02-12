from ...device import SimDevice


class BogusDevice(SimDevice):
    """Class for devices compatible with Bogus-Bus."""

    category = "bogus_device"


# Servo device classes
class ServoDevice(BogusDevice):
    category = "servo_devices"


class BogusV1ServoDevice(ServoDevice, BogusDevice):
    category = "bogus_v1_servo"
    test_category = "bogus_v1_servo"


class BogusV2ServoDevice(ServoDevice, BogusDevice):
    category = "bogus_v2_servo"
    test_category = "bogus_v2_servo"


class BogusV1Servo(BogusV1ServoDevice):
    name = "bogo_v1_servo"
    model_id = 0xB0905000


class BogusV2Servo(BogusV2ServoDevice):
    name = "bogo_v2_servo"
    model_id = 0xB0905001


# IO module classes
class IODevice(BogusDevice):
    category = "io_devices"


class BogusV1IODevice(IODevice, BogusDevice):
    category = "bogus_v1_io"
    test_category = "bogus_v1_io"


class BogusV1IO(BogusV1IODevice):
    name = "bogo_v1_io"
    model_id = 0xB0901000
