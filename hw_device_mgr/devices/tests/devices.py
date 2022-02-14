from ...lcec.device import LCECSimDevice
from ..elmo_gold import ElmoGold420, ElmoGold520
from ..inovance_is620n import InovanceIS620N
from ..inovance_sv660 import InovanceSV660


class DevicesForTest(LCECSimDevice):
    category = "devices_for_test"


class ElmoGold420ForTest(DevicesForTest, ElmoGold420):
    name = "elmo_gold_0x30924_0x10420_test"
    test_category = "elmo_gold_420_test"


class ElmoGold520ForTest(DevicesForTest, ElmoGold520):
    name = "elmo_gold_0x30925_0x10420_test"
    test_category = "elmo_gold_520_test"


class InovanceIS620NForTest(DevicesForTest, InovanceIS620N):
    name = "IS620N_ECAT_test"
    test_category = "inovance_sv660n_test"


class InovanceSV660NForTest(DevicesForTest, InovanceSV660):
    name = "SV660_ECAT_test"
    test_category = "inovance_is620n_test"
