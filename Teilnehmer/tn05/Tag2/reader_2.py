
"""
Search for ips
"""

import re

FILE_PATH = '/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log'
IP_REGEX = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

def read_file(path: str)->str:
    '''
    description
    '''
    with open(path, "r") as file_descriptor:
        log = file_descriptor.read()
        return log

def search_ip_adress(log: str, pattern_ip: str)->list:
    '''
    description
    '''
    found_ip_adresses = []
    matches = re.finditer(pattern_ip, log, re.MULTILINE)
    for i in matches:
        found_ip_adresses.append(i.group())
    return found_ip_adresses

if __name__ == "__main__":
    print(search_ip_adress(read_file(FILE_PATH), IP_REGEX))