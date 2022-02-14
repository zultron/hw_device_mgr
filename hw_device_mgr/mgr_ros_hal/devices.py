# Real devices under LCEC
from ..hal.device import HALPinDevice
from ..lcec.device import LCECDevice, LCECSimDevice
from ..cia_402.device import CiA402Device, CiA402SimDevice
from ..devices.elmo_gold import ElmoGold420, ElmoGold520
from ..devices.inovance_is620n import InovanceIS620N
from ..devices.inovance_sv660 import InovanceSV660
from ..devices.bogus import BogusServo


class ManagedDevices(LCECDevice, CiA402Device, HALPinDevice):
    category = "managed_lcec_devices"


class ElmoGold420LCEC(ManagedDevices, ElmoGold420):
    name = "elmo_gold_420_lcec"


class ElmoGold520LCEC(ManagedDevices, ElmoGold520):
    name = "elmo_gold_520_lcec"


class InovanceIS620NLCEC(ManagedDevices, InovanceIS620N):
    name = "inovance_is620n_lcec"


class InovanceSV660LCEC(ManagedDevices, InovanceSV660):
    name = "inovance_sv660n_lcec"


class SimManagedLCECDevices(LCECSimDevice, CiA402SimDevice, HALPinDevice):
    category = "sim_lcec_managed_devices"


class BogusServoSimLCEC(SimManagedLCECDevices, BogusServo):
    name = "bogus_servo_drive_sim_lcec"


class ElmoGold420SimLCEC(SimManagedLCECDevices, ElmoGold420):
    name = "elmo_gold_420_sim_lcec"


class ElmoGold520SimLCEC(SimManagedLCECDevices, ElmoGold520):
    name = "elmo_gold_520_sim_lcec"


class InovanceIS620NSimLCEC(SimManagedLCECDevices, InovanceIS620N):
    name = "inovance_is620n_sim_lcec"


class InovanceSV660SimLCEC(SimManagedLCECDevices, InovanceSV660):
    name = "inovance_sv660n_sim_lcec"
