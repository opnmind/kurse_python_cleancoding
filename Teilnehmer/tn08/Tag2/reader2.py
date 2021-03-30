#!/usr/bin/env python3
"""
Find IP addresses in a file
"""

import re

REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


def read_log(_log):
    """
    Read content from logfile
    """
    with open(_log, "r") as file_descriptor:
        return file_descriptor.read()


def find_ip_addresses(_log, pattern=REGEX):
    """
    Find IP addresses according to regex pattern
    """
    _ip_addresses = []

    matches = re.finditer(pattern, _log)

    for match in matches:
        _ip_addresses.append(match.group())

    return _ip_addresses


def print_result(_ip_addresses):
    """
    Print the result
    """
    print(_ip_addresses)


if __name__ == "__main__":
    LOGFILE = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    log = read_log(LOGFILE)
    ip_addresses = find_ip_addresses(log)
    print_result(ip_addresses)
