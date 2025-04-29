#CS 431/528 Final
#D.Gamarra 
#SUNY POLY SPRING 2025


import os
from scapy.all import rdpcap, UDP

def parse_eqemu_pcap(file_path):
    packets = rdpcap(file_path)
    print(f"Loaded {len(packets)} packets from {file_path}.")

    #Create 'data' directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    #Construct output file path inside 'data'
    base_name = os.path.basename(file_path).rsplit(".", 1)[0]
    output_file = os.path.join("data", f"{base_name}_output.dat")

    with open(output_file, "w") as f:
        f.write(f"Loaded {len(packets)} packets from {file_path}.\n")
        f.write("Packet#" + "\t"+ "Optcode" + "\t"+ "Length"+ "\t" + "First 10 Bytes" + "\t\t\t" + "Time"+"\n" ) 
        
        # Parse the packets
        for i, pkt in enumerate(packets):
            if UDP in pkt:
                udp_payload = bytes(pkt[UDP].payload)
                if len(udp_payload) >= 2:
                    opcode = int.from_bytes(udp_payload[0:2], byteorder='little')
                    f.write(f"{i}\t{hex(opcode)}\t{len(udp_payload)}\t{udp_payload[:10].hex(' ')}\t{pkt.time}\n")
                    #f.write(f"Packet #{i}:\n")
                    #f.write(f"  Timestamp: {pkt.time}\n")
                    #f.write(f"  UDP Payload Length: {len(udp_payload)} bytes\n")
                    #f.write(f"  Opcode: {hex(opcode)}\n")
                    #f.write(f"  First 10 Bytes: {udp_payload[:10].hex(' ')}\n")
                    #f.write("-" * 40 + "\n")

    print(f"Packet analysis saved to {output_file}")
# Have the command be able to run in the terminal with spesifying the given packet capture file 
# This is so i dont spend time having to edit every intance of the fullpath of the file
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("\n")
        print("Hey you don’t have Packages! I Cannot Read anything :( ")
        print("Usage: python3 SCRIPT.py your_capture.pcapng")
        print()
    else:
        parse_eqemu_pcap(sys.argv[1])

