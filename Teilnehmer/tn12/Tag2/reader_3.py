# pylint: disable=C0326
"""
Class style
"""
import re

class LogfileIPFinder:
    """Class to work with Logfile"""

    PATTERN_IP4 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    def __init__(self, file):
        """ Init Class """
        self._ip_adresses = []
        self._read_logfile(file)

    def _read_logfile(self, file):
        """ Read Logfile """
        with open(file) as file_pointer:
            self._logfile = file_pointer.read()

    def _search_regx(self, regx_pattern):
        """ Search Regx Pattern in Logfile """
        matches = re.finditer(regx_pattern, self._logfile, re.MULTILINE)

        for match in matches:
            self._ip_adresses.append(match.group())

    def __str__(self):
        """__str__"""
        return "Meine Innern Werte" # TODO

    def __repr__(self):
        """__repr__"""
        return str(self) # TODO

    def get_ip4_adresses(self):
        """ Print out IP adresses """
        self._search_regx(self.PATTERN_IP4)
        return self._ip_adresses

    def get_ip6_adresses(self):
        """ Docstring """
        return self._ip_adresses


if __name__ == "__main__":
    PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    logfile_1 = LogfileIPFinder(PATH)
    print(logfile_1.get_ip4_adresses())
