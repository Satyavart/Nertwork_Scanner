#!usr/bin/env python
import scapy.all as scapy
import argparse


def argument():
    par = argparse.ArgumentParser()
    par.add_argument("-t", "--target", dest="target", help="IP address of destination")
    options = par.parse_args()
    return options.target


def print_dest(dest_list):
    print("IP\t\t\tMAC Address\n------------------------------------------")
    for client in dest_list:
        print(client["ip"] + "\t\t" + client["mac"])


def send(ip, mac):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=mac)
    broadcast_arp_request = broadcast/arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


virtual_mac = "ff:ff:ff:ff:ff:ff"
destination_IP = argument()
scanned_list = send(destination_IP, virtual_mac)
print_dest(scanned_list)