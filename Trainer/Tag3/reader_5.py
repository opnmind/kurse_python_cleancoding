"""
Modul IP Finder

Eine Erklärung was heir passiert

Ein Aufrufbeispiel

Verweise
"""
import typing
import re

class Reader:
    def __init__(self, filename):
        self._filename = filename

    def read(self):
        with open(self._filename) as fd:
            return fd.read()

class IpFinder:
    '''
    Klassendokumentation
    '''
    PATTERN_IP: str = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    def __init__(self, filereader: Reader, pattern_ip: str=None) -> None:
        """ Docstring """
        self.filereader = filereader
        self.pattern_ip = pattern_ip if pattern_ip else self.PATTERN_IP
        self._log_data: str = ""
        self._adresses: list = []

    def get_log_data(self):
        """DocString"""
        return self._log_data.split("\n")

    def read_log(self, filereader: Reader=None) -> 'IpFinder':
        '''
        Funktionsname:
        '''
        if filereader:
            self.filereader = filereader
        self._log_data = self.filereader.read()
        return self

    def find_ip_adresses(self, pattern_ip: str=None) -> 'IpFinder':
        '''
        Funktionsname:
        '''
        if not pattern_ip:
            pattern_ip = self.pattern_ip
        matches = re.finditer(pattern_ip, self._log_data, re.MULTILINE)
        self._adresses = [match.group() for match in matches]
        return self


    def get_ip_adresses(self) -> list: 
        '''
        Funktionsname:
        '''
        return self._adresses

if __name__ == "__main__":
    #FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    #
    #print(IpFinder(Reader(FILE_PATH)).
    #      read_log().
    #      find_ip_adresses().
    #      get_ip_adresses())
    
    import unittest
    from unittest.mock import Mock

    reader = Mock()
    reader.read.return_value = "Willi\n127.0.0.1\n"

    print(IpFinder(reader).
          read_log().
          find_ip_adresses().
          get_ip_adresses())

