#!/usr/bin/python3


import time
import sys


class Port():
    def calc_rx(self):
        if self.oper_state == "down":
            return "disabled"
        elif self.port_state[6] == '1':
            return "defaulted"
        elif self.port_state[7] == '1':
            return "expired"
        elif self.sys_mac.count('0') != 16:
            return "current"

    def __str__(self):
        return ("\nPort\t\tRole\tSystem prio\t\tID\t\tPort prio\tPort num\tOper key\tPort state\trx_state\n" +
                self.name[0:3] + '..' + self.name[-3::] + '\tactor\t' + self.sys_prio + '\t\t' + self.sys_mac + '\t\t' + self.port_prio + 
                '\t\t' + self.port_number + '\t\t' + self.port_key + '\t\t' + self.port_state + '\t' +
                self.rx_state + '\n' +
                '\t\tpartner\t' + self.partner.sys_prio + '\t\t' + self.partner.sys_mac + '\t\t' + self.partner.port_prio +
                '\t\t' + self.partner.port_number + '\t\t' + self.partner.oper_key + '\t\t' + self.partner.port_state + '\n')


class Args():
    def __init__(self):
        self.debug = False


def open_status(filename: str):
    with open(filename, "r") as file:
        return file.read()


def parse_status(filedata: str, args: Args, last_ports: list):
    ports = []
    i = 24
    splited = filedata.split('\n')

    while i < len(splited):
        current_port = Port()
        current_port.partner = Port()

        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.name = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.oper_state = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1

        i+=11

        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.sys_prio = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.sys_mac = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_key = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_prio = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_number = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_state = ''.join(reversed(str(bin(int(value)))[2::])) + '0' * (10 - len(str(bin(int(value)))))
        print(splited[i]) if args.debug else print("", end='')
        i+=1

        i+=1

        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.sys_prio = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.sys_mac = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.oper_key = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.port_prio = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.port_number = value
        print(splited[i]) if args.debug else print("", end='')
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.port_state = ''.join(reversed(str(bin(int(value)))[2::])) + '0' * (10 - len(str(bin(int(value)))))
        print(splited[i]) if args.debug else print("", end='')
        
        i+=1

        current_port.rx_state = current_port.calc_rx()
        ports.append(current_port)
        i+=1

    if not last_ports:
        for port in ports:
            print(port)
    else:
        for i in range(len(last_ports)):
            for j in range(len(ports)):
                if (ports[j].name == last_ports[i].name and ports[j].rx_state != last_ports[i].rx_state):
                    print(ports[j])
    
    return ports



def main():
    args = Args()
    if '-d' in sys.argv:
        args.debug = True

    ports = parse_status(open_status(FILEPATH), args, None)
    while 1:
        time.sleep(0.1)
        ports = parse_status(open_status(FILEPATH), args, ports)


FILEPATH = "/proc/net/bonding/bond0"
main()
