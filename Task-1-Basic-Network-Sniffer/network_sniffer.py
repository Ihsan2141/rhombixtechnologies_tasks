from scapy.all import sniff, IP, TCP, UDP

packet_count = 0

def process_packet(packet):
    global packet_count

    if packet.haslayer(IP):
        packet_count += 1

        protocol = "Other"

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"

        print("\n========================")
        print(f"Packet Number : {packet_count}")
        print(f"Source IP     : {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol      : {protocol}")

print("Network Sniffer Started...")
print("Press CTRL+C to Stop\n")

sniff(prn=process_packet, store=False)


