from scapy.all import rdpcap

def extract_latency(pcap_file):
    packets = rdpcap(pcap_file)
    times = [pkt.time for pkt in packets if pkt.haslayer('ICMP')]
    if len(times) >= 2:
        return times[1] - times[0]  
#dilen- this gives a rough RTT estimate
    return None


