"""
Script IP finder

Erklärung

Aufrufbeispiel

Verweise
"""
import re

LOG_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

with open(LOG_PATH, "r") as file_descriptor:
    log = file_descriptor.read()
print(len(log))
found_ip_addresses = []
matches = re.findall(PATTERN_IP, log, re.MULTILINE)

for match in matches:
    print(match)
    found_ip_addresses.append(match.group())

print(found_ip_addresses)
