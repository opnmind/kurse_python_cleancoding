#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Logfile IP Finder
"""

import sys
import re


class LogfileIPReader:
    """ Class LogfileIPReader. """
    _REGEX_PATTERN_IPV4 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    _REGEX_PATTERN_IPV6 = r"\[(?:[a-zA-Z0-9]{0,4}:?){1,8}\]|\[(?:[a-zA-Z0-9]{0,4}:?){1,4}(?:[0-9]{1,3}\.){3}[0-9]{1,3}\]"
    _ip_addresses = []
    _log = None
    _ipv6 = None

    def __init__(self, filename, ipv6=False):
        """ Constructor. """
        self._filename = filename
        self._ipv6 = ipv6

    def run(self):
        """ Runner. """
        self._read_log_file()
        self._analyse_log_file()
        self._print_findings()

    def _read_log_file(self):
        """ Read the Logfile. """
        try:
            with open(self._filename, "r") as file_descriptor:
                self._log = file_descriptor.read()
        except OSError as err:
            print(f"OS error: {err}")
        except:
            print(f"Unexpected error: {sys.exc_info()[0]}")

    def _analyse_log_file(self):
        """ Analyse the Logfile. """
        if not self._ipv6:
            pattern = self._REGEX_PATTERN_IPV4
        else:
            pattern = self._REGEX_PATTERN_IPV6

        matches = re.finditer(pattern, self._log, re.MULTILINE)
        self._ip_addresses = [match.group() for match in matches]
        self._ip_addresses = sorted(self._ip_addresses)

    def _print_findings(self):
        """ Print out the Findings. """
        for ip_address in self._ip_addresses:
            print(f"{ip_address}")

    def __str__(self):
        """ Stringify List """
        return ', '.join(self._ip_addresses)
