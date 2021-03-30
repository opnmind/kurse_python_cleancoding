"""
This is a test-reader to get ip-addresses out of a log-file and print the
addresses found to stdout, one address per line.
"""

import re
from itertools import starmap

LOG_FILE = '/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log'
IP_SEARCH_PATTERN = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

with open(LOG_FILE, 'r') as log_file_reader:
    log_file_content = log_file_reader.read()

ip_addresses = re.findall(IP_SEARCH_PATTERN, log_file_content, re.MULTILINE)
enumerated_ip_addresses = enumerate(ip_addresses)
formatted_lines_for_print = starmap(lambda i, item: f'{i}: {item}', enumerated_ip_addresses)

print('\n'.join(formatted_lines_for_print))
