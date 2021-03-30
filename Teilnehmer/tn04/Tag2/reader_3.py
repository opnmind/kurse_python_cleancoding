"""
Modul IP Finder

Description
Example
"""
import re

class IpFinder:
    '''
    TEST
    '''
    PATTERN_IP = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    def __init__(self, file_path, pattern_ip=None):
        '''
        TEST
        '''
        self.file_path = file_path
        self.file_pathlog_data = None
        self.adresses = None
        self.log_data = None
        self.pattern_ip = pattern_ip if pattern_ip else self.PATTERN_IP

    def read_log(self, file_path=None):
        '''
        TEST
        '''
        if file_path:
            self.file_path = file_path
        with open(self.file_path, "r") as file_descriptor:
            self.log_data = file_descriptor.read()
        return self

    def find_ip_adresses(self, pattern_ip=None):
        '''
        TEST
        '''
        if not pattern_ip:
            pattern_ip = self.pattern_ip
        matches = re.finditer(pattern_ip, self.log_data, re.MULTILINE)
        self.adresses = [match.group() for match in matches]
        return self

    def get_ip_adresses(self):
        '''
        TEST
        '''
        return self.adresses

if __name__ == "__main__":
    FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    
    print(IpFinder(FILE_PATH).
        read_log().
        find_ip_adresses().
        get_ip_adresses())
