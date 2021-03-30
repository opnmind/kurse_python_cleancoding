"""
Function Style
"""
import re

PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
PATTERN_IP = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def read_ip_adresses(file):
    with open(file, "r") as file_pointer:
        logfile = file_pointer.read()

    print(len(logfile))
    ip_adresses = []

    matches = re.finditer(PATTERN_IP, logfile, re.MULTILINE)

    for match in matches:
        ip_adresses.append(match.group())

    return ip_adresses

if __name__ == "__main__":
    ip_adresses = read_ip_adresses(PATH)
    print(ip_adresses)