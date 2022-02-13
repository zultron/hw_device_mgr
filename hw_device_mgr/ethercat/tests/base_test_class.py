from ...cia_402.tests.base_test_class import BaseCiA402TestClass
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
import re
import pytest


class BaseEtherCATTestClass(BaseCiA402TestClass):

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
    sdo_model_id_clone = tuple(
        [EtherCATSimConfig.format_model_id(mid) for mid in
         (
             (0x00B090C0, 0xB0905030),
             (0x00B090C0, 0xB0905031),
             (0x00B090C0, 0xB0901030),
         )
        ]
    )
    load_device_sdos_yaml = False  # SDO data from ESI file

    @property
    def model_id_clone_map(self):
        return dict(zip(self.sdo_model_id_clone, self.device_model_classes))

    @pytest.fixture
    def device_xml(self, tmp_path):
        if self.device_class is BogusEtherCATDevice:
            yield
        elif self.device_class is not BogusEtherCATDevice:
            # Subclasses will have different product_code, so customize ESI file
            self.device_class.set_device_xml_dir(tmp_path)
            finished_paths = set()
            re_str = '|'.join(fr'{pc[1]:08X}' for pc in self.sdo_model_id_clone)
            re_str = r'#x(' + re_str + r')'
            pat = re.compile(re_str)
            # Map of orig ESI file product code to new ESI file product code
            cm = {k[1]:v.device_model_id()[1] for k,v in self.model_id_clone_map.items()}
            repl = lambda m: f'#x{cm[int(m.group(1), 16)]}'
            for id_orig, cls in self.model_id_clone_map.items():
                esi_orig = cls.orig_xml_description_path()
                esi_new = cls.xml_description_path()
                if esi_orig in finished_paths:
                    continue
                finished_paths.add(esi_orig)
                esi_new.parent.mkdir(exist_ok=True)
                with open(esi_orig) as f_orig:
                    with open(esi_new, "w") as f_new:
                        for line in f_orig:
                            line = pat.sub(repl, line)
                            f_new.write(line)
                print(f"Wrote ESI file to {esi_new}")
                print(f"  Original in {esi_orig}")
            yield

    @pytest.fixture
    def extra_fixtures(self, device_xml):
        # Use this to add extra fixtures to the `device_cls` fixture
        # in subclasses
        pass
