"""
Modul IP Finder

Description
Example
"""
import re

FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def read_log():
    '''
    TEST
    '''
    with open(FILE_PATH, "r") as file_descriptor:
        return file_descriptor.read()

def find_ip_adresses(log, pattern_ip=PATTERN_IP):
    '''
    TEST
    '''
    found_ip_adresses = []
    matches = re.finditer(pattern_ip, log, re.MULTILINE)

    for match in matches:
        found_ip_adresses.append(match.group())
    return found_ip_adresses

def show_ip_adresses(ip_adresses):
    '''
    TEST
    '''
    print(ip_adresses)

if __name__ =="__main__":
    log = read_log()
    ip_adresses = find_ip_adresses(log)
    show_ip_adresses(ip_adresses)
