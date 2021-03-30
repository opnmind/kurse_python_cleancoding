#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Logfile IP Finder
"""
from lib.logfile_ip_reader_v2 import LogfileIPReader


if __name__ == "__main__":
    FILENAME = "./data/Sample.log"
    logIPReader = LogfileIPReader(filename=FILENAME)
    logIPReader.run()
