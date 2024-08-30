import struct

# Function to parse BPB data from a hexadecimal string
def parse_bpb(hex_input):
    # Convert the hex string to bytes
    bpb_bytes = bytes.fromhex(hex_input)

    # Define BPB structure according to FAT file system
    bpb_structure = {
        "Jump Boot Code": bpb_bytes[0:3].hex(),
        "OEM Name/Version": bpb_bytes[3:11].decode('ascii'),
        "Bytes Per Sector": struct.unpack_from("<H", bpb_bytes, 11)[0],
        "Sectors Per Cluster": struct.unpack_from("<B", bpb_bytes, 13)[0],
        "Reserved Sectors": struct.unpack_from("<H", bpb_bytes, 14)[0],
        "Number of FATs": struct.unpack_from("<B", bpb_bytes, 16)[0],
        "Max Root Directory Entries": struct.unpack_from("<H", bpb_bytes, 17)[0],
        "Total Sectors (16-bit)": struct.unpack_from("<H", bpb_bytes, 19)[0],
        "Media Descriptor": struct.unpack_from("<B", bpb_bytes, 21)[0],
        "Sectors Per FAT (16-bit)": struct.unpack_from("<H", bpb_bytes, 22)[0],
        "Sectors Per Track": struct.unpack_from("<H", bpb_bytes, 24)[0],
        "Number of Heads": struct.unpack_from("<H", bpb_bytes, 26)[0],
        "Hidden Sectors": struct.unpack_from("<I", bpb_bytes, 28)[0],
        "Total Sectors (32-bit)": struct.unpack_from("<I", bpb_bytes, 32)[0]
    }

    return bpb_structure

# Get user input for the hexadecimal string
hex_input = input("Enter the hexadecimal string: ")

# Ensure the input length is a multiple of 2 (valid hex string)
if len(hex_input) % 2 != 0:
    print("Invalid hexadecimal string length. Must be an even number of characters.")
else:
    # Parse and display the BPB structure
    bpb_structure = parse_bpb(hex_input)
    for key, value in bpb_structure.items():
        print(f"{key}: {value}")
