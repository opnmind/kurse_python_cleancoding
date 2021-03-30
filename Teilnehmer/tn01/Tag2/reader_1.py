#!/usr/bin/env python3

import re


# with open('/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log', 'r') as lgs:
#         content = lgs.readlines()
#         ips = re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', content, re.MULTILINE)
#         ip_list = []
#         for line in ips:
#             ip_list.append(ips.group())
#         print(ip_list)

source_file = '/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log'
regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open(source_file, 'r') as param:
    lines = param.readlines()
    all_ips = re.finditer(regex, lines, re.MULTILINE)
    for entry in all_ips:
        found_ips = []
        found_ips.append(all_ips.group())
        print(found_ips)
