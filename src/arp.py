'''
Sample script to send an ARP who-is to an IP range
'''
import scapy
from scapy.sendrecv import sendp, sniff, srp
from scapy.all import Ether, ARP

# broadcast message
eth = Ether(dst = "ff:ff:ff:ff:ff:ff")

# IP range in prefix notation - first 24 bits are left unchanged
arp = ARP(pdst = '192.168.137.0/24')

# send and recieve multiple packets
answered, unanswered = srp(eth / arp)
for pkt in answered:
	print pkt
