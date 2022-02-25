#!/usr/bin/env python3

# https://www.kollmorgen.com/sites/default/files/How%20to%20capture%20and%20use%20WireShark%20trace%20data%20with%20EtherCAT%20applications.pdf
#
# RxPDO/bitlen:  6040/2, 6060/1, 607A/4, 60FE.01/4
# TxPDO/bitlen:  6041/2, 6061/1, 6064/4, 6077/2, 6078/2, 60FD/4, 1002/4, 603F/2
# Data from EtherCAT datagram LRW command:
#   0f00080000000000000000371208ffffffff0800080008003f0010c846000000
# Command:
# $0 0f00080000000000000000371208ffffffff0800080008003f0010c846000000 2 1 4 4 2 1 4 2 2 4 4 2
import os
import sys
import re
import enum
import pyshark

# $0 /home/zultron/elmo.2022-02-24.ethercat_switch_on_disabled.pcapng

class PDO(int):
    def __new__(cls, number, base=10, **kwargs):
        return super().__new__(cls, number, base)

    def __init__(self, x, base=10, *, pdo, length):
        self.pdo = pdo
        self.length = length

    def __str__(self):
        return f"0x{{:0{int(self.length)*2}X}}".format(self)

    def __repr__(self):
        return f"<PDO {self.pdo}={str(self)}>"

class EcatDecoder:

    class ecat_cmd(enum.IntEnum):
        # https://infosys.beckhoff.com/content/1033/tc3_io_intro/1257993099.html
        NOP=0
        APRD=1
        APWR=2
        APRW=3
        FPRD=4
        FPWR=5
        FPRW=6
        BRD=7
        BWR=8
        BRW=9
        LRD=10
        LWR=11
        LRW=12
        ARMW=13
        # Above link doesn't list FRMW, but pcap dissectors do
        FRMW=14

    def __init__(self, fname, pdos):
        self.fname = fname
        self.pdos = pdos

    def timestamp_diff(self, pkt1, pkt2):
        diff = float(pkt1.sniff_timestamp) - float(pkt2.sniff_timestamp)
        return int(diff * 1e9)

    def print_obj(self, obj, maxlen=500):
        for attr in dir(obj):
            if attr.startswith('_'):
                continue
            try:
                val = repr(getattr(obj, attr))
            except Exception as e:
                print(f"{attr}:  (Couldn't get repr)")
            else:
                val = val if len(val) < maxlen else val[:maxlen]
                print(f"{attr}:  {val}")

    datagram_attr_re = re.compile(r'^sub([0-9]+)_([a-z]+)$')

    def layer_datagrams(self, layer):
        datagrams = dict()
        for attr in layer.field_names:
            m = self.datagram_attr_re.match(attr)
            if m:
                ix, field = m.groups()
                datagram = datagrams.setdefault(ix, dict(ix=ix))
                datagram[field] = getattr(layer, attr)
        for ix, datagram in datagrams.items():
            datagram['cmd'] = self.ecat_cmd(int(datagram.pop('cmd'), 16))
            yield datagram

    def decode_lrw_pdos(self, datagram):
        assert datagram['cmd'] == self.ecat_cmd.LRW
        assert 'data' in datagram
        data = datagram['data']
        raw = data.raw_value
        # Reverse octets so values are in correct order
        octets = ''.join(raw[i-2:i] for i in range(len(raw), 0, -2))
        res = dict()
        for pdo, length in self.pdos:
            # PDO values are in reverse order; pull values off end
            res[pdo] = PDO(octets[-length*2:], base=16, pdo=pdo, length=length)
            octets = octets[:-length*2]
            # res.append(int(octets[:length*2], 16))
            # octets = octets[length*2:]
        assert octets == ""
        return res

    def delta_stats(self, deltas):
        avg_p = int(sum(deltas) / len(deltas))
        min_p = min(d for d in deltas if d > 0)
        max_p = max(deltas)
        return avg_p, min_p, max_p

    def read_packets(self):
        cap = pyshark.FileCapture(self.fname)
        prev_pkt = None
        deltas = list()
        for count, pkt in enumerate(cap):
            ethercat_layer = pkt.layers[0]
            assert ethercat_layer.layer_name == "eth"
            if ethercat_layer.src_lg == '0':
                # Ignore packets from controller (slaves send packets with 'lg'
                # bit set; maybe not reliable if master does that, but why would
                # it?)
                continue

            ecat_layers = [l for l in pkt.layers if l.layer_name == "ecat"]
            if not ecat_layers:
                continue  # Skip packets without EtherCAT layers

            td = ""
            if prev_pkt:
                deltas.append(self.timestamp_diff(pkt, prev_pkt))
                td = f"  time delta (ns): {deltas[-1]}"
            print(f"Packet #{count}:{td}")
            # print(pkt)
            # print("time:", pkt.sniff_timestamp)
            # self.print_obj(ethercat_layer)
            for layer in ecat_layers:
                # print("layer.subframe_length:", layer.subframe_length)
                # self.print_obj(layer)
                for d in self.layer_datagrams(layer):
                    # print(f"sub{d.pop('ix')}:")
                    # for k, v in d.items():
                    #     print(f"  {k}:  {repr(v)}")
                    if d['cmd'] == self.ecat_cmd.LRW:
                        print("  LRW cmd PDOs:")
                        for k, v in self.decode_lrw_pdos(d).items():
                            print(f"    {k}:  {v}")
                # layer.pretty_print()
                # if layer.cmd == 0xC

            prev_pkt = pkt
            # if count > 4:
            #     break

        avg_p, min_p, max_p = self.delta_stats(deltas)
        print(f"Update period stats:  avg={avg_p}, min={min_p}, max={max_p}")

if __name__ == '__main__':
    fname = sys.argv[1]
    assert os.path.exists(fname), f"File '{fname}' doesn't exist"
    pdos = [
        ('6040h', 2),
        ('6060h', 1),
        ('607Ah', 4),
        ('60FE-01h', 4),
        ('6041h', 2),
        ('6061h', 1),
        ('6064h', 4),
        ('6077h', 2),
        ('6078h', 2),
        ('60FDh', 4),
        ('1002h', 4),
        ('603Fh', 2),
    ]

    d = EcatDecoder(fname, pdos)
    d.read_packets()

    # orig, counts = sys.argv[1], sys.argv[2:]
    # res = decode(orig, *counts)
    # print(orig)
    # print(''.join(orig[i-2:i] for i in range(len(orig), 0, -2)))
    # print(' '.join(f"0x{{:0{int(l)*2}X}}".format(r) for r,l in zip(res, counts)))
