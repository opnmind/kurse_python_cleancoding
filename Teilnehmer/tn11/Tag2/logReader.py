"""
Get IPs from Logfile
"""
import re
import sys


IPV4_REGEX_PATTERN = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


def read_file(file_name):
    """
    Returns the file as string
    """
    with open(file_name, "r") as opened_file:
        file_data = opened_file.read()
        return file_data


def extract_ips(text):
    """
    Returns a list of all ips from a string
    """
    ips = []
    matches = re.finditer(IPV4_REGEX_PATTERN, text, re.MULTILINE)
    for match in matches:
        ips.append(match.group())
    return ips


def print_list(input_list):
    """
    Prints the whole list
    """
    for list_item in input_list:
        print(list_item)


if __name__ == "__main__":
    FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"

    try:
        file = read_file(FILE_PATH)
    except FileNotFoundError:
        print("Could not load file")
        sys.exit()

    ips = extract_ips(file)
    print_list(ips)
