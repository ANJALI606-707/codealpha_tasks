from scapy.all import sniff, conf

# Use Layer 3 socket (works on Windows without WinPcap)
conf.L3socket

# Function to process only IPv4 packets
def packet_callback(packet):
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        print(f"🌐 IPv4 Packet -> Source: {src_ip} | Destination: {dst_ip} | Protocol: {packet.proto}")

# Capture IPv4 packets only
def main():
    print("🔍 Listening for IPv4 packets... Press Ctrl+C to stop.\n")
    sniff(prn=packet_callback, store=False, filter="ip")

if __name__ == "__main__":  # Corrected here
    main()
