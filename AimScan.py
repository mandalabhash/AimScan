import argparse
import pyfiglet
from datetime import datetime
from AimSSTI import ssti_scan
from AimLFI import lfi_scan
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def print_banner():
    banner = pyfiglet.figlet_format("AimScan", font="slant")
    print(Fore.GREEN + banner + Style.RESET_ALL)

def scan_target(url):
    start_time = datetime.now()

    print_banner()
    print(Fore.YELLOW + "Welcome to AimScan - Web Pentesting Tool" + Style.RESET_ALL)
    print(Fore.WHITE + f"Scanning target: {url}" + Style.RESET_ALL)

    # SSTI scanning
    print(Fore.CYAN + "Scanning for SSTI vulnerabilities..." + Style.RESET_ALL)
    ssti_vulns = ssti_scan(url)
    if ssti_vulns:
        print(Fore.RED + "SSTI vulnerabilities found:" + Style.RESET_ALL)
        for vuln in ssti_vulns:
            print(f"- Payload: {vuln[0]}, URL: {vuln[1]}, Status: {vuln[2]}")
    else:
        print(Fore.GREEN + "No SSTI vulnerabilities found." + Style.RESET_ALL)

    # LFI scanning
    print(Fore.CYAN + "Scanning for LFI vulnerabilities..." + Style.RESET_ALL)
    lfi_vulns = lfi_scan(url)
    if lfi_vulns:
        print(Fore.RED + "LFI vulnerabilities found:" + Style.RESET_ALL)
        for vuln in lfi_vulns:
            print(f"- Payload: {vuln[0]}, URL: {vuln[1]}, Status: {vuln[2]}")
    else:
        print(Fore.GREEN + "No LFI vulnerabilities found." + Style.RESET_ALL)

    end_time = datetime.now()
    total_time = end_time - start_time
    print(Fore.WHITE + f"Scan completed. Total time taken: {total_time}" + Style.RESET_ALL)

    # Log file name
    ssti_log_file = f"{url.split('//')[1].split('.')[0]}_ssti_log.txt"
    lfi_log_file = f"{url.split('//')[1].split('.')[0]}_lfi_log.txt"
    print(Fore.CYAN + f"SSTI log file: {ssti_log_file}" + Style.RESET_ALL)
    print(Fore.CYAN + f"LFI log file: {lfi_log_file}" + Style.RESET_ALL)

    return ssti_vulns, lfi_vulns

def main():
    parser = argparse.ArgumentParser(description="Web Pentesting Tool")
    parser.add_argument("url", nargs="?", type=str, help="Target URL")
    args = parser.parse_args()

    if args.url:
        ssti_vulns, lfi_vulns = scan_target(args.url)
        return ssti_vulns, lfi_vulns
    else:
        print_banner()
        print(Fore.YELLOW + "Welcome to AimScan - Web Pentesting Tool" + Style.RESET_ALL)
        print(Fore.WHITE + "Please provide the target URL as a command-line argument." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
