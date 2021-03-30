"""
Modul IP Finder

Description
Example
"""
import re

FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

with open(FILE_PATH, "r") as file_descriptor:
    log = file_descriptor.read()
found_ip_adresses = []

matches = re.finditer(PATTERN_IP, log, re.MULTILINE)

for matchNUM, match in enumerate(matches, start=1):
    found_ip_adresses.append(match.group())

print(found_ip_adresses)
