
# AimScan

## Introduction
AimScan is a Web Pentesting Tool designed for educational purposes and academic requirements. It helps in identifying vulnerabilities like Server-Side Template Injection (SSTI) and Local File Inclusion (LFI) in web applications.

## Functions
- Scans for SSTI vulnerabilities using various payloads.
- Scans for LFI vulnerabilities using common traversal sequences.
- Provides reports if thw guven domain vulnerable to SSTI or LFI or both.
- Colorful CLI output for better visualization.
- Logs the scan results for further analysis inti text files.

## Requirements
- Python 3
- colorama
- requests
- beautifulsoup4
- pyfiglet

Install the required packages using `pip3 install -r requirements.txt`.

## Installation Commands
Clone the repository:
```bash
git clone https://github.com/mandalabhash/AimScan.git
```

Change directory:
```bash
cd AimScan
```

Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Usage
Run the AimScan tool using the following command:
```bash
python3 AimScan.py <target-url>
```

Replace `<target-url>` with the URL of the website you want to scan.

## Output
The tool generates reports of SSTI and LFI vulnerabilities found during the scan. It also logs the scan results in separate files for further analysis.

## Disclaimer
AimScan is intended for educational purposes only. The authors are not responsible for any misuse or damage caused by this tool. Use it responsibly and only on websites you have permission to scan.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

