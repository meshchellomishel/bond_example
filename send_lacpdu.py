#!/usr/bin/python3.10


from scapy.all import *
from scapy.layers.inet import Ether, Dot3
from scapy.contrib.lacp import SlowProtocol, LACP
import socket


LACP_ACTIVITY = 0x01
LACP_TIMEOUT = 0x02
LACP_AGGREGATION = 0x04
LACP_SYNCHRONYZATION = 0x08
LACP_COLLECTING = 0x16
LACP_DISTRIBUTING = 0x32
LACP_DEFAULTED = 0x64
LACP_EXPIRED = 0x128

LACP_DEFAULT_ACTOR_STATE = LACP_ACTIVITY | LACP_AGGREGATION | LACP_SYNCHRONYZATION | LACP_DEFAULTED


class Lacp_obj():
    def __init__(self):
        self.ac_sys_prio = 1
        self.ac_sys_mac = '70:85:c2:b3:c7:26'
        self.ac_port_key = 1
        self.ac_port_prio = 1
        self.ac_port_num = 4
        self.ac_state = LACP_DEFAULT_ACTOR_STATE

        self.pt_sys_prio = 65535
        self.pt_sys_mac = '00:00:00:00:00:00'
        self.pt_port_key = 1
        self.pt_port_prio = 255
        self.pt_port_num = 1
        self.pt_state = LACP_ACTIVITY


def build_pkt():
    pkt = (Ether(src='70:85:c2:b3:c7:26', dst='00:00:00:00:00:00')
            / SlowProtocol() / LACP(actor_system_priority=1, actor_system='70:85:c2:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=4,
                                    actor_state=LACP_DEFAULT_ACTOR_STATE))
    return pkt


def main():
    sendp(build_pkt, 'eth11', 4)


main()