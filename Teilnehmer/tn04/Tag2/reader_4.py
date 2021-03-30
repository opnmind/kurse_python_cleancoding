"""
Modul IP Finder

Eine Erklärung was heir passiert

Ein Aufrufbeispiel

Verweise
"""
import typing
import re



class IpFinder:
    '''
    Klassendokumentation
    '''
    PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    def __init__(self, file_path: str, pattern_ip: str=None) -> None:
        """ Docstring """
        self.file_path = file_path
        self.log_data: str = ""
        self.adresses: list = []
        self.pattern_ip = pattern_ip if pattern_ip else self.PATTERN_IP

    def read_log(self, file_path: str="") -> object:
        '''
        Funktionsname:
        '''
        if file_path:
            self.file_path = file_path
        with open(self.file_path, "r") as file_descriptor:
            self.log_data = file_descriptor.read()
        return self

    def find_ip_adresses(self, pattern_ip: str="") -> object:
        '''
        Funktionsname:
        '''
        if not pattern_ip:
            pattern_ip = self.pattern_ip
        matches = re.finditer(pattern_ip, self.log_data, re.MULTILINE)
        self.adresses = [match.group() for match in matches]
        return self


    def get_ip_adresses(self) -> list:
        '''
        Funktionsname:
        '''
        return self.adresses

if __name__ == "__main__":
    FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"

    print(IpFinder(FILE_PATH).
          read_log().
          find_ip_adresses().
          get_ip_adresses())
    