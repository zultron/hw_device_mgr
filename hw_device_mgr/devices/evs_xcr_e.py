from ..ethercat.device import EtherCATDevice
from ..cia_402.device import CiA402Device


class EVSXCRE(EtherCATDevice, CiA402Device):
    """Ingenia Everest S XCR-E servo drive."""

    vendor_id = 0x0000029C
    product_code = 62066689
    xml_description_package = "hw_device_mgr.devices.device_xml"
    xml_description_fname = "evs-xcr-e_esi.xml"
    device_error_package = "hw_device_mgr.devices.device_err"
    device_error_yaml = "unpopulated.yaml"
