#!/usr/bin/python3

from scapy.all import *

target = input("Informe um alvo: ")
destport = input("Porta de destino: ")

port = int(destport)

ans,unans=sr(IP(dst=target, ttl=(1, 30))/TCP(dport=port, flags="s"))
ans.sumary(lambda s,r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))


