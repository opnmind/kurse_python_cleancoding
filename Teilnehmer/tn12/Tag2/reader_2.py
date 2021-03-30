"""
Module IP Finder extended with functions

Erklaerung

Aufrufbeispiel

Verweise
"""
import re

LOG_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

def read_log_file(file_path):
    '''
    Funktionsbeschreibung
    '''
    with open(file_path, "r") as file_descriptor:
        log = file_descriptor.read()

    return log

def find_ip_addesses(search_text, search_pattern):
    '''
    Funktionsbeschreibung
    '''
    found_ip_addresses = []

    matches = re.findall(search_pattern, search_text, re.MULTILINE)

    for match in matches:
        found_ip_addresses.append(match)

    return found_ip_addresses

def show_ip_addresses(found_matches):
    '''
    Funktionsbeschreibung
    '''
    print(found_matches)

log_result = read_log_file(LOG_PATH)
filtered_matches = find_ip_addesses(log_result, PATTERN_IP)
show_ip_addresses(filtered_matches)
