#!/usr/bin/env python3
"""
Find IP addresses in a file
"""

import re

LOGFILE = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

with open(LOGFILE, "r") as file_descriptor:
    log = file_descriptor.read()

ip_addresses = []

matches = re.finditer(REGEX, log)

for match in matches:
    ip_addresses.append(match.group())

print(ip_addresses)
