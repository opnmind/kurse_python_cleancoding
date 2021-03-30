#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Logfile IP Finder
"""

import sys
import re

import LogfileError

class LogfileIPReader:
    """ Class LogfileIPReader. """
    _REGEX_PATTERN_IPV4: str = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    _REGEX_PATTERN_IPV6: str = r"\[(?:[a-zA-Z0-9]{0,4}:?){1,8}\]|\[(?:[a-zA-Z0-9]{0,4}:?){1,4}(?:[0-9]{1,3}\.){3}[0-9]{1,3}\]"
    _ip_addresses: list = [str]
    _log: str = None
    _ipv6: bool = None

    def __init__(self, filename: str, ipv6: bool=False) -> None:
        """ Constructor. """
        self._filename: str = filename
        self._ipv6: bool = ipv6

    def run(self)  -> None:
        """ Runner. """
        self._read_log_file()
        self._analyse_log_file()
        self._print_findings()

    def _read_log_file(self, os_errorhandler=None, all_errorhandler=None) -> None:
        """ Read the Logfile. """
        try:
            with open(self._filename, "r") as file_descriptor:
                self._log = file_descriptor.read()
        except FileNotFoundError as err:
            pass
            #raise LogfileError(f"File not found: {err}")

    def _analyse_log_file(self) -> None:
        """ Analyse the Logfile. """
        if not self._ipv6:
            pattern = self._REGEX_PATTERN_IPV4
        else:
            pattern = self._REGEX_PATTERN_IPV6

        matches = re.finditer(pattern, self._log, re.MULTILINE)
        self._ip_addresses = [match.group() for match in matches]
        self._ip_addresses = sorted(self._ip_addresses)

    def _print_findings(self) -> None:
        """ Print out the Findings. """
        for ip_address in self._ip_addresses:
            print(f"{ip_address}")

    def __str__(self) -> str:
        """ Stringify List """
        return ', '.join(self._ip_addresses)

def common_errorhandler(e, obj):
    print("Error: ", e, " in ", obj)
