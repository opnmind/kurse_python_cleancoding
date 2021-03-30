"""
Get IPs from Logfile
"""
import re
import sys


class log_reader:
    """
    Documentaion
    """

    
    IPV4_REGEX_PATTERN = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    file_path = ""
    def __init__(self, path):
        self.file_path = path

    def read_file(self):
        """
        Returns the file as string
        """
        with open(self.file_path, "r") as opened_file:
            file_data = opened_file.read()
            return file_data


    def extract_ips(self, text):
        """
        Returns a list of all ips from a string
        """
        ips = []
        matches = re.finditer(self.IPV4_REGEX_PATTERN, text, re.MULTILINE)
        for match in matches:
            ips.append(match.group())
        return ips


    def print_list(self, input_list):
        """
        Prints the whole list
        """
        for list_item in input_list:
            print(list_item)


if __name__ == "__main__":
    FILE_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    
    log_instance = log_reader(FILE_PATH)

    try:
        file = log_instance.read_file()
    except FileNotFoundError:
        print("Could not load file")
        sys.exit()

    ips = log_instance.extract_ips(file)
    log_instance.print_list(ips)
