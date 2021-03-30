"""
Modul IP-Finder

test

test
"""
import re

FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

with open(FILE_PATH, "r") as file_descriptor:
    log = file_descriptor.read()

found_ip_adresses = []
matches = re.finditer(PATTERN_IP, log, re.MULTILINE)

for i in matches:
    #print(i)
    found_ip_adresses.append(i.group())

print(found_ip_adresses)