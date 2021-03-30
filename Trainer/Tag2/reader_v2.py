#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Logfile IP Finder
"""

import sys
import re


class LogfileIPReader:
    """ Class LogfileIPReader. """
    _REGEX_PATTERN_IPV4: str = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    _REGEX_PATTERN_IPV6: str = r"\[(?:[a-zA-Z0-9]{0,4}:?){1,8}\]|\[(?:[a-zA-Z0-9]{0,4}:?){1,4}(?:[0-9]{1,3}\.){3}[0-9]{1,3}\]"
    _ip_addresses: list = [str]
    _log: str = None
    _ipv6: bool = None
    _os_errorhandler = None
    _all_errorhandler = None

    def __init__(self, filename: str, ipv6: bool=False) -> None:
        """ Constructor. """
        self._filename: str = filename
        self._ipv6: bool = ipv6

    def set_os_errorhandler(self, os_errorhandler):
        self._os_errorhandler = os_errorhandler 
        return self

    def set_all_errorhandler(self, all_errorhandler):
        self._all_errorhandler = all_errorhandler 
        return self

    def run(self)  -> None:
        """ Runner. """
        self._read_log_file()
        self._analyse_log_file()
        self._print_findings()

    def _read_log_file(self) -> None:
        """ Read the Logfile. """
        try:
            with open(self._filename, "r") as file_descriptor:
                self._log = file_descriptor.read()
        except OSError as err:
            if self._os_errorhandler:
                self._os_errorhandler(err)
            else:
                raise err
        except Exception as e:
            if self._all_errorhandler:
                self._all_errorhandler(e)
            else:
                raise e

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

def common_errorhandler(e): # Ein Testbeispiel
    print("Logging: Error: -->", se, "<--")
    exit(1)

def file_errorhandler(e):
    print("File not found")

if __name__ == "__main__":
    lf = LogfileIPReader(
            filename = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.lög"
         ).set_os_errorhandler(
             file_errorhandler
         ).set_all_errorhandler(
             common_errorhandler
         )
    # nur für den Test:
    lf._read_log_file()
    print("Es geht weiter")
    #lf.run()

