from ...cia_301.tests.base_test_class import BaseCiA301TestClass, BaseTestClass
from ..data_types import EtherCATDataType
from ..sdo import EtherCATSDO
from ..command import EtherCATSimCommand
from ..config import EtherCATSimConfig
from .bogus_devices.device import (
    BogusEtherCATDevice,
    BogusEtherCATServo,
    BogusOtherCATServo,
    BogusEtherCATIO,
)


class BaseEtherCATTestClass(BaseCiA301TestClass):

    # Classes under test in this module
    data_type_class = EtherCATDataType
    sdo_class = EtherCATSDO
    command_class = EtherCATSimCommand
    config_class = EtherCATSimConfig
    device_class = BogusEtherCATDevice
    device_model_classes = (
        BogusEtherCATServo,
        BogusOtherCATServo,
        BogusEtherCATIO,
    )
    sdo_model_id_clone = (
        (0x00B090C0, 0xB0905030),
        (0x00B090C0, 0xB0905031),
        (0x00B090C0, 0xB0901030),
    )
    load_device_sdos_yaml = False  # SDO data from ESI file

    def init_sim(self):
        # Init sim device data, SDOs and device config
        super().init_sim()
        # ESI may not match test devices, but we want to reuse it
        # - Build map of ESI model ID equivalents
        sdos = self.config_class._model_sdos
        model_ids = [dc.device_model_id() for dc in self.device_model_classes]
        sdo_map = dict(zip(model_ids, self.sdo_model_id_clone))
        # - Copy SDO equivalents for any missing device
        for device_class in self.device_model_classes:
            model_id = device_class.device_model_id()
            if model_id in sdos:
                continue  # Good, already there
            else:
                sdos[model_id] = sdos[sdo_map[model_id]]
