# Boot Sector and BIOS Parameter Block (BPB) Parser

This repository contains a Python script for parsing the BIOS Parameter Block (BPB) data from a hexadecimal string. The script reads a hexadecimal string representing the BPB and extracts various fields according to the FAT file system specifications.

## Script Overview

The script converts a hexadecimal string into bytes and parses the BPB structure, including:
- Jump Boot Code
- OEM Name/Version
- Bytes Per Sector
- Sectors Per Cluster
- Reserved Sectors
- Number of FATs
- Max Root Directory Entries
- Total Sectors (16-bit)
- Media Descriptor
- Sectors Per FAT (16-bit)
- Sectors Per Track
- Number of Heads
- Hidden Sectors
- Total Sectors (32-bit)

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bpb-parser.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd bpb-parser
    ```
   
3. Run the script:
    ```bash
    python bpb_parser.py
    ```

4. Enter the hexadecimal string when prompted. The script will display the parsed BPB fields on separate lines.

## Example

```bash
Enter the hexadecimal string: EB52904E5446532020202000020800000000000000F800003F00FF00802004000000000080008000FF3F060000000000AA420000000000000200000000000000
```

Output:
```
Jump Boot Code: eb52
OEM Name/Version: NTF
Bytes Per Sector: 512
Sectors Per Cluster: 8
Reserved Sectors: 2
Number of FATs: 2
Max Root Directory Entries: 512
Total Sectors (16-bit): 2880
Media Descriptor: 248
Sectors Per FAT (16-bit): 9
Sectors Per Track: 63
Number of Heads: 255
Hidden Sectors: 0
Total Sectors (32-bit): 0
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements or bug fixes.

