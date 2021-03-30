"""
This is a test-reader to get ip-addresses out of a log-file and print the
addresses found to stdout, one address per line.
"""

import re
import sys
from pathlib import Path
from itertools import starmap
from typing import Union, List, Tuple


IP_SEARCH_PATTERN = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'


def read_log_file_lines(log_file_path: Union[Path,str] = None):
    """Reads a text-based log-file and returns its contents
    Args:
        log_file_path (str or Path-like): representing the path to the log-file to be read.

    Returns:
        log_file_content: multiline string with data read from log-file

    """    
    if log_file_path is not None:
        _log_file_path = Path(log_file_path)
        if _log_file_path.is_file():
            with open(log_file_path, 'r') as log_file_reader:
                for line in log_file_reader:
                    yield line           
        else:
            print(f'File {_log_file_path} not found.')
            sys.exit(2)

def get_ip_addresses(content_line: str = None, search_pattern: str = IP_SEARCH_PATTERN):
    """Extracts a list of ip-addesses as string from a line of text (usually from a log-file)
    Args:
        content_line (str): input line read from text file, which will be searched for ip addresses
        search_pattern (str): regex search pattern matching ip adresses, defaults to r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    Returns:
        list of ip addresses or None if no address was found
    """
    return re.findall(search_pattern, content_line, re.MULTILINE)


def print_ip_addresses(ip_addresses: List[str] = None, counter : int = 0 ):
    """Prints a list of ip addresses if ip addresses where foun in the given line
    Args:
        ip_addresses (List(str)): List of ip addresses as string
        counter (int): current ip address counter status 

    Returns:
        counter (int): counter updated with the number of ip addresses printed
    """
    if ip_addresses is not None and len(ip_addresses) > 0:
        formatted_lines_for_print = starmap( lambda _counter, item: f'{_counter}: {item}', enumerate( ip_addresses, counter ))
        print('\n'.join(formatted_lines_for_print))
        return counter + len(ip_addresses)
    else:
        return counter



if __name__ == "__main__":

    LOG_FILE = '/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log'
    
    counter = 1
    for content_line in read_log_file_lines(LOG_FILE):
        ip_addresses = get_ip_addresses(content_line)
        counter = print_ip_addresses(ip_addresses=ip_addresses, counter=counter)

