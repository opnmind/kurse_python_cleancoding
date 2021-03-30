"""
Modul IP Finder

Eine Erklärung was hier passiert

Ein Aufrufbeispiel

Verweise
"""
import re
from pathlib import Path
from typing import Sequence



class IpFinder:
    '''
    Klassendokumentation
    '''
    PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    def __init__(self, file_path: Path = Path(), pattern_ip: str = "") -> None:
        """ Docstring """
        self.file_path: Path = file_path
        self.log_data: str = ""
        self.adresses: Sequence[str] = list()
        self.pattern_ip: str = pattern_ip if pattern_ip else self.PATTERN_IP

    def read_log(self, file_path: Path = Path()) -> 'IpFinder':
        '''
        Funktionsname:
        '''
        if file_path:
            self.file_path = file_path
        with open(self.file_path, "r") as file_descriptor:
            self.log_data = file_descriptor.read()
        return self

    def find_ip_adresses(self, pattern_ip: str = "") -> 'IpFinder':
        '''
        Funktionsname:
        '''
        if not pattern_ip:
            pattern_ip = self.pattern_ip
        matches = re.finditer(pattern_ip, self.log_data, re.MULTILINE)
        self.adresses = [match.group() for match in matches]
        return self


    def get_ip_adresses(self) -> Sequence[str]:
        '''
        Funktionsname:
        '''
        return self.adresses

if __name__ == "__main__":
    FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"

    print(IpFinder(Path(FILE_PATH)).
          read_log().
          find_ip_adresses().
          get_ip_adresses())
    