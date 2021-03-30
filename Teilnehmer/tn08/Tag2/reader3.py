#!/usr/bin/env python3
"""
Find IP addresses in a file
"""
import re


class Reader:
    """
    The Reader class
    """

    REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    def __init__(self, log, regex=None):
        self._ip_addresses = []
        self._read_log(log)
        self.regex = regex if regex else self.REGEX

    def _read_log(self, log):
        """
        Read content from logfile
        """
        with open(log, "r") as file_descriptor:
            self._log = file_descriptor.read()

    def find_ip_addresses(self, pattern):
        """
        Find IP addresses according to regex pattern
        """
        matches = re.finditer(pattern, self._log)

        for match in matches:
            self._ip_addresses.append(match.group())

    def return_result(self):
        """
        Print the result
        """
        self.find_ip_addresses(self.regex)
        return self._ip_addresses


if __name__ == "__main__":
    LOGFILE = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    print(Reader(LOGFILE).return_result())
