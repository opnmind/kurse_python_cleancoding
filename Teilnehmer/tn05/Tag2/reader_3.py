
"""
Search for ips
"""

import re



class IpFinder:
    '''
    Class-Documentation
    '''
    IP_REGEX = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    def __init__(self, file_path, pattern_ip=None):
        """
        Docstring
        """
        self.file_path = file_path
        self.log = None
        self.pattern_ip = pattern_ip if pattern_ip else self.IP_REGEX
        self.found_ip_adresses = []

    def read_file(self, file_path=None):
        '''
        description
        '''      
        if file_path:
            self._file_path = file_path
        with open(self.file_path, "r") as file_descriptor:
            self.log = file_descriptor.read()
        return self


    def search_ip_adress(self, pattern_ip=None):
        '''
        description
        '''
        if not pattern_ip:
            pattern_ip=self.pattern_ip
        matches = re.finditer(pattern_ip, self.log, re.MULTILINE)
        for i in matches:
            self.found_ip_adresses.append(i.group())
        return self.found_ip_adresses

if __name__ == "__main__":
    FILE_PATH = '/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log'

    print(IpFinder(FILE_PATH).read_file().search_ip_adress())