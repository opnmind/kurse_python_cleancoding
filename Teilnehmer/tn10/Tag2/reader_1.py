"""
Module IP Finder

Blug und Hugo

History:
30.03.2021 author    init
"""
import re

PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

with open(PATH, "r") as file_pointer:
    logfile = file_pointer.read()

print(len(logfile))
ip_adresses = []

matches = re.finditer(PATTERN_IP, logfile, re.MULTILINE)

for match in matches:
    ip_adresses.append(match.group())

print(ip_adresses)
