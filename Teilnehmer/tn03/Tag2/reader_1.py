#!/usr/bin/python3
"""
This moodule provides the possibility to search for IP's in logfiles
"""
import re
from typing import List

class LogIpReader:
    """
    LogIPReader
    """
    def __init__(self, logpath):
        self._logpath = logpath
        self._read_all(logpath)


    def _read_all(self, logpath: str = None) -> str:
        """
        Reads configfile
        """

        with open(logpath, "r") as logile:
            self._log_content = logile.read()
        return self._log_content


    def search_for_ip(self, pattern: str = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}") -> List[str]:
        """
        search for IP addresses
        """
        self.ip_findings = re.findall(pattern, self._log_content)
        return self.ip_findings


    def make_unique(self, ips: List[str]) -> List[str]:
        """
        make IP's unique
        """
        return set(ips)


if __name__ == "__main__":
    FILEPATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    logreader = LogIpReader(FILEPATH)
    logreader.search_for_ip()
    candidates = make_unique(candidates)
    for candidate in candidates:
        print(candidate)
