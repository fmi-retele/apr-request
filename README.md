# arp-request
#### Make an arp request with scapy
##### Requirements:
- use any linux or use the [Ubuntu x64 vbox machine](https://github.com/fmi-retele/vbox-scapy/releases/download/v1/osbox.vdi.tar.gz)
- check that you have [scapy](http://www.secdev.org/projects/scapy/) installed
- check the [ARP](http://www.networksorcery.com/enp/protocol/arp.htm) header 
- for scapy, check [this](https://thepacketgeek.com/scapy-p-05-sending-our-first-packet-arp-response/) tutorial
- [RFC826](http://www.networksorcery.com/enp/rfc/rfc826.txt)
The world is a jungle in general, and the networking game contributes many animals.  At nearly every layer of a network
architecture there are several potential protocols that could be used.  For example, at a high level, there is TELNET and SUPDUP for remote login.  Somewhere below that there is a reliable byte stream protocol, which might be CHAOS protocol, DOD TCP, Xerox BSP or DECnet.  Even closer to the hardware is the logical transport layer, which might be CHAOS, DOD Internet, Xerox PUP, or DECnet.  The 10Mbit Ethernet allows all of these protocols (and more) to coexist on a single cable by means of a type field in the Ethernet packet header.  However, the 10Mbit Ethernet requires 48.bit addresses on the physical cable, yet most protocol addresses are not 48.bits long, nor do they necessarily have any relationship to the 48.bit Ethernet address of the hardware.  For example, CHAOS addresses are 16.bits, DOD Internet addresses are 32.bits, and Xerox PUP addresses are 8.bits.  A protocol is needed to dynamically distribute the correspondences between a <protocol, address> pair and a 48.bit Ethernet address.

