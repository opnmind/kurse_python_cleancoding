"""
Modul IP Finder

Eine Erklärung was heir passiert

Ein Aufrufbeispiel

Verweise
"""
import re


PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

def read_log(file_path):
    '''
    Funktionsname:
    '''
    with open(file_path, "r") as file_descriptor:
        return file_descriptor.read()


def find_ip_adresses(log_data, pattern_ip=PATTERN_IP):
    '''
    Funktionsname:
    '''
    matches = re.finditer(pattern_ip, log_data, re.MULTILINE)
    return [match.group() for match in matches]


def show_ip_adresses(adresses):
    '''
    Funktionsname:
    '''
    print(adresses)

if __name__ == "__main__":
    FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    log = read_log(FILE_PATH)
    ip_adresses = find_ip_adresses(log)
    show_ip_adresses(ip_adresses)
