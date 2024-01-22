#!/usr/bin/python3


import time
import pandas as pd


RX_EXPIRED = 0x128
RX_DEFAULTED = 0x64


class Port():
    def calc_rx(self):
        if self.port_state[6] == '1':
            return "defaulted"
        elif self.port_state[7] == '1':
            return "expired"
        elif self.sys_mac.count('0') != 16 and self.oper_state != "down":
            return "current"
        else:
            return "disabled"

    def __str__(self):
        return ("\nPort\tRole\tSystem prio\t\tID\t\tPort prio\tPort num\tOper key\tPort state\trx_state\n" +
                self.name + '\t' + 'actor\t' + self.sys_prio + '\t\t' + self.sys_mac + '\t\t' + self.port_prio + 
                '\t\t' + self.port_number + '\t\t' + self.port_key + '\t\t' + self.port_state + '\t' +
                self.calc_rx() + '\n' +
                '\tpartner\t' + self.partner.sys_prio + '\t\t' + self.partner.sys_mac + '\t\t' + self.partner.port_prio +
                '\t\t' + self.partner.port_number + '\t\t' + self.partner.oper_key + '\t\t' + self.partner.port_state + '\n')


def open_status(filename: str):
    with open(filename, "r") as file:
        return file.read()


def parse_status(filedata: str):
    ports = []
    i = 24
    splited = filedata.split('\n')

    while i < len(splited):
        current_port = Port()
        current_port.partner = Port()

        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.name = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.oper_state = value
        i+=1

        i+=11

        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.sys_prio = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.sys_mac = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_key = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_prio = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_number = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.port_state = ''.join(reversed(str(bin(int(value)))[2::])) + '0' * (10 - len(str(bin(int(value)))))
        i+=1

        i+=1

        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.sys_prio = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.sys_mac = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.oper_key = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.port_prio = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.port_number = value
        i+=1
        value = "".join(splited[i].split(':')[1::]).split(" ")[1]
        current_port.partner.port_state = ''.join(reversed(str(bin(int(value)))[2::])) + '0' * (10 - len(str(bin(int(value)))))
        
        i+=1

        ports.append(current_port)
        i+=1

    
    for port in ports:
        print(port)



def main():
    time.sleep(0.1)
    parse_status(open_status(FILEPATH))


FILEPATH = "/proc/net/bonding/bond0"
main()
