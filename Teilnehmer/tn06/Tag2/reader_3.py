"""
Module IP Finder extended with functions

Erklaerung

Aufrufbeispiel

Verweise
"""
import re

class IpFinder:
    ''' Klassendefinition '''

    def __init__(self, file_path, pattern_ip=None):
        self.file_path = file_path
        self.pattern_ip = pattern_ip if pattern_ip else PATTERN_IP
        self.log_data = None

    def read_log_file(self, file_path=None):
        ''' Funktionsbeschreibung '''
        if not file_path:
            file_path = self.file_path
        with open(file_path, "r") as file_descriptor:
            self.log_data = file_descriptor.read()
        return self

    def find_ip_addesses(self, search_text=None, search_pattern=None):
        ''' Funktionsbeschreibung '''
        found_ip_addresses = []
        if not search_pattern:
            search_pattern = self.pattern_ip
        if not search_text:
            search_text = self.log_data
        matches = re.findall(search_pattern, search_text, re.MULTILINE)
        for match in matches:
            found_ip_addresses.append(match)

        return found_ip_addresses

    def show_ip_addresses(self, found_matches):
        ''' Funktionsbeschreibung '''
        return found_matches

if __name__ == "__main__":
    LOG_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    PATTERN_IP = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    myIpFinder = IpFinder(LOG_PATH)
    log_result = myIpFinder.read_log_file()
    filtered_matches = myIpFinder.find_ip_addesses()
    print(myIpFinder.show_ip_addresses(filtered_matches))
