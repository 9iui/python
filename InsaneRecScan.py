import os
import subprocess
import sys

# Color codes
GREEN = '\033[0;32m'
REDIN = '\033[0;31m'
YELLO = '\033[0;33m'
NC = '\033[0m'  # No color

# Function to print the banner
def print_banner():
    print(f"{GREEN}#########################################################{NC}")
    print(f"{GREEN}#                                                       #{NC}")
    print(f"{REDIN}#                  InsaneRecScan.py                     #{NC}")
    print(f"{GREEN}#                                                       #{NC}")
    print(f"{YELLO}#           Developed by Nithin Kumar                   #{NC}")
    print(f"{GREEN}#            https://github.com/Nithin-X                #{NC}")
    print(f"{GREEN}#                                                       #{NC}")
    print(f"{GREEN}#########################################################{NC}")

# Output directory
output_dir = "InsaneReconScan"

# Check if output directory exists
if os.path.exists(output_dir):
    print(f"Error: {output_dir} already exists.")
    sys.exit(1)

# Create output directory
os.mkdir(output_dir)
print(f"Output directory created: {output_dir}\n")

# Change to output directory
os.chdir(output_dir)

# Call the print_banner function
print_banner()

# Check if argument is provided
if len(sys.argv) < 2:
    print("Syntax Error: python InsaneRecScan.py <Domain>")
    sys.exit(1)

# Define target domain
target = sys.argv[1]
print(f"Scanning the Domain: {target}\n")

# Output files
open_ports_file = "open_ports.txt"
vulnerabilities_file = "vulnerabilities.txt"
directories_file = "directories.txt"
nikto_report = "nikto_report.txt"
whatweb_report = "whatweb_report.txt"

# Run Nmap scan to find open ports
print("Scanning for open ports...")
nmap_output = subprocess.run(["nmap", "-p-", "-T4", target], capture_output=True, text=True).stdout
open_ports = [line.split('/')[0] for line in nmap_output.splitlines() if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))]
with open(open_ports_file, "w") as file:
    file.write(','.join(open_ports))
print(f"Open ports saved to {open_ports_file}")

# Run Nmap scan using the gathered open ports
print("Scanning with Nmap using the gathered open ports...")
nmap_output = subprocess.run(["nmap", "-p", ','.join(open_ports), "-A", target], capture_output=True, text=True).stdout
with open(vulnerabilities_file, "w") as file:
    file.write(nmap_output)
print(f"Nmap scan vulnerabilities saved to {vulnerabilities_file}")

# Run Gobuster to find directories
print("Scanning for directories with Gobuster...")
gobuster_output = subprocess.run(["gobuster", "dir", "-u", f"http://{target}", "-w", "/usr/share/wordlists/dirb/common.txt", "-e", "-x", "html,php,zip,js"], capture_output=True, text=True).stdout
with open(directories_file, "w") as file:
    file.write(gobuster_output)
print(f"Gobuster directories saved to {directories_file}")

# Run Nikto to find vulnerabilities
print("Scanning for vulnerabilities with Nikto...")
nikto_output = subprocess.run(["nikto", "-h", target, "-output", nikto_report], capture_output=True, text=True).stdout
nikto_vulnerabilities = [line[2:] for line in nikto_output.splitlines() if line.startswith('+ ')]
with open(vulnerabilities_file, "a") as file:
    file.write('\n'.join(nikto_vulnerabilities))
print(f"Nikto vulnerabilities saved to {vulnerabilities_file}")

# Run WhatWeb to find vulnerabilities
print("Scanning for vulnerabilities with WhatWeb...")
whatweb_output = subprocess.run(["whatweb", target], capture_output=True, text=True).stdout
whatweb_vulnerabilities = [line.split(': ')[1] for line in whatweb_output.splitlines() if '[+]' in line]
with open(vulnerabilities_file, "a") as file:
    file.write('\n'.join(whatweb_vulnerabilities))
print(f"WhatWeb vulnerabilities saved to {vulnerabilities_file}")

print(f"{GREEN}#########################################################{NC}")
print(f"{GREEN}#                                                       #{NC}")
print(f"{GREEN}# InsaneRecScan.py #                                    #{NC}")
print(f"{REDIN}# SCAN COMPLETED!!! #                                   #{NC}")
print(f"{GREEN}#                                                       #{NC}")
print(f"{GREEN}#########################################################{NC}")
