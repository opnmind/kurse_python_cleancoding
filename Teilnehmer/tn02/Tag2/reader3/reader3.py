"""
This is a test-reader to get ip-addresses out of a log-file and print the
addresses found to stdout, one address per line.
"""

import re
import sys
from pathlib import Path
from itertools import starmap
from typing import Union, List, AnyStr


IP_SEARCH_PATTERN = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'


class LogFile:
    """Represents a log file from which lines are read lazily
    """
    def __init__(self, log_file_path: Union[Path, str] = None):
        """Initializes a logfile with a file path to the file on local filesystem
        Args:
            log_file_path (str or Path-like): representing the path to the log-file to be read.
        """
        self._log_file_path = log_file_path

    def read_lines(self):
        """Reads the text-based log-file as initialized on class creation and returns its contents

        Returns:
            log_file_content: yields data from log-file line by line
        """
        if self._log_file_path is not None:
            try:
                with open(self._log_file_path, 'r') as log_file_reader:
                    for line in log_file_reader:
                        yield line
            except OSError as file_exception:
                print(f'File {self._log_file_path} could not be opened. {file_exception}')
                sys.exit(2)


class IPAdressManager:
    """Encapsulate ip address extraction """
    def get_ip_addresses(self, content_line: str = None, search_pattern: str = IP_SEARCH_PATTERN):
        """Extracts a list of ip-addesses as string from a line of text (usually from a log-file)
        Args:
            content_line (str): input line read from text file, which will be searched for ip addresses
            search_pattern (str): regex search pattern matching ip adresses, defaults to standard search pattern

        Returns:
            list of ip addresses or None if no address was found
        """
        return re.findall( search_pattern, content_line, re.MULTILINE)


class IPAddressPrinter:
    """Encapsulate ip address printing function"""
    def print_ip_addresses(self, ip_addresses: List[str] = None, counter: int = 0):
        """Prints a list of ip addresses if ip addresses where foun in the given line
        Args:
            ip_addresses (List(str)): List of ip addresses as string
            counter (int): current ip address counter status

        Returns:
            counter (int): counter updated with the number of ip addresses printed
        """
        if ip_addresses is not None and len(ip_addresses) > 0:
            formatted_lines_for_print = starmap(lambda _counter, item: f'{_counter}: {item}', enumerate(ip_addresses, counter))
            print('\n'.join(formatted_lines_for_print))
            return counter + len(ip_addresses)
        else:
            return counter



if __name__ == "__main__":

    LOG_FILE = '/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log'

    counter = 1
    log_file = LogFile(LOG_FILE)
    ip_address_manager = IPAdressManager()
    ip_address_printer = IPAddressPrinter()
    for content_line in log_file.read_lines():
        ip_addresses = ip_address_manager.get_ip_addresses(content_line)
        counter = ip_address_printer.print_ip_addresses(ip_addresses=ip_addresses, counter=counter)
