#!/usr/bin/python3


from time import *
from scapy.all import *
from scapy.layers.inet import Ether, Dot3
from scapy.contrib.lacp import SlowProtocol, LACP
import socket


LACP_ACTIVITY = 1
LACP_TIMEOUT = 2
LACP_AGGREGATION = 4
LACP_SYNCHRONYZATION = 8
LACP_COLLECTING = 16
LACP_DISTRIBUTING = 32
LACP_DEFAULTED = 64
LACP_EXPIRED = 128

LACP_DEFAULT_ACTOR_STATE = LACP_ACTIVITY | LACP_AGGREGATION | LACP_SYNCHRONYZATION | LACP_DEFAULTED


def send_lacp(lacp):
    pkt = (Ether() / SlowProtocol() / lacp)
    sendp(pkt, 'enp30s0', 1)


def slep():
    sleep(5)


def next_test(msg):
    slep()
    print("[TEST]: ", msg)


def partner_settings_test():
    next_test("--- system ID test")
    lacp = LACP(actor_system_priority=999, actor_system='99:99:99:b3:c7:26',
                                    actor_key=999, actor_port_priority=999, actor_port_number=999,
                                    actor_state=LACP_DEFAULT_ACTOR_STATE)
    send_lacp(lacp)

    slep()
    lacp = LACP(actor_system_priority=999, actor_system='11:11:11:b3:c7:26',
                                    actor_key=999, actor_port_priority=999, actor_port_number=999,
                                    actor_state=LACP_DEFAULT_ACTOR_STATE)
    send_lacp(lacp)

    next_test("--- system priority test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=999, actor_port_priority=999, actor_port_number=999,
                                    actor_state=LACP_DEFAULT_ACTOR_STATE)
    send_lacp(lacp)

    next_test("--- key test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=999, actor_port_number=999,
                                    actor_state=LACP_DEFAULT_ACTOR_STATE)
    send_lacp(lacp)

    next_test("--- port priority test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=999,
                                    actor_state=LACP_DEFAULT_ACTOR_STATE)
    send_lacp(lacp)

    next_test("--- port nuber test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_DEFAULT_ACTOR_STATE)
    send_lacp(lacp)


def partner_states_test():
    next_test("--- activity test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_ACTIVITY)
    send_lacp(lacp)

    next_test("--- timeout test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_TIMEOUT)
    send_lacp(lacp)

    next_test("--- aggregation test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_AGGREGATION)
    send_lacp(lacp)

    next_test("--- synchronization test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_SYNCHRONYZATION)
    send_lacp(lacp)

    next_test("--- collecting test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_COLLECTING)
    send_lacp(lacp)

    next_test("--- distributing test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_DISTRIBUTING)
    send_lacp(lacp)

    next_test("--- expired test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_EXPIRED)
    send_lacp(lacp)

    next_test("--- defaulted test")
    lacp = LACP(actor_system_priority=1, actor_system='11:11:11:b3:c7:26',
                                    actor_key=1, actor_port_priority=1, actor_port_number=1,
                                    actor_state=LACP_DEFAULTED)
    send_lacp(lacp)


def main():
    print("[SETTINGS test]")
    partner_settings_test()
    print("[STATE test]")
    partner_states_test()


main()
