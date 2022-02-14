# Real devices under LCEC
from ..hal.device import HALPinDevice, HALDataType
from ..lcec.device import LCECDevice, LCECSimDevice
from ..cia_402.device import CiA402Device, CiA402SimDevice
from ..ethercat.device import EtherCATSimDevice
from ..devices.elmo_gold import ElmoGold420, ElmoGold520
from ..devices.inovance_is620n import InovanceIS620N
from ..devices.inovance_sv660 import InovanceSV660
from ..devices.bogus import BogusV1Servo, BogusV2Servo


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


class SimManagedEtherCATDevices(
    EtherCATSimDevice, CiA402SimDevice, HALPinDevice
):
    category = "sim_ethercat_managed_devices"
    data_type_class = HALDataType


class BogusV1ServoSimLCEC(SimManagedEtherCATDevices, BogusV1Servo):
    name = "bogus_v1_servo_drive_sim_ethercat"


class BogusV2ServoSimLCEC(SimManagedEtherCATDevices, BogusV2Servo):
    name = "bogus_v2_servo_drive_sim_ethercat"


class ElmoGold420SimLCEC(SimManagedEtherCATDevices, ElmoGold420):
    name = "elmo_gold_420_sim_ethercat"


class ElmoGold520SimLCEC(SimManagedEtherCATDevices, ElmoGold520):
    name = "elmo_gold_520_sim_ethercat"


class InovanceIS620NSimLCEC(SimManagedEtherCATDevices, InovanceIS620N):
    name = "inovance_is620n_sim_ethercat"


class InovanceSV660SimLCEC(SimManagedEtherCATDevices, InovanceSV660):
    name = "inovance_sv660n_sim_ethercat"
