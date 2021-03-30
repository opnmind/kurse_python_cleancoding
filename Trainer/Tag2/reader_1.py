"""
Modul IP Finder

Eine Erklärung was heir passiert

Ein Aufrufbeispiel

Verweise
"""
import re

FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

with open(FILE_PATH, "r") as file_descriptor:
    log = file_descriptor.read()

found_ip_adresses = []
matches = re.finditer(PATTERN_IP, log, re.MULTILINE)

for match in matches:
    found_ip_adresses.append(match.group())

print(found_ip_adresses)
