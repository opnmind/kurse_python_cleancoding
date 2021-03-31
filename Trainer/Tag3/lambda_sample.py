#
""" Docstring"""

import re

def read_from_file(file_name, text_filter=None):
    """ Docstring """
    with open(file_name) as file_descriptor:
        lines = file_descriptor.read().split("\n")
    if text_filter:
        lines = [line for line in lines if text_filter(line)]
    return lines

def ip4_only(line): # Filter als echte Funktion
    """Dostring"""
    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    return re.findall(pattern, line)


if __name__ == "__main__":
    FILE_NAME = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    ip4_filter = lambda line: re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)

    text = read_from_file(FILE_NAME, ip4_only)
    print(len(text))

    text = read_from_file(FILE_NAME, ip4_filter)
    print(len(text))
