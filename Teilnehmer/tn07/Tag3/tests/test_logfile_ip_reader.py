import sys
sys.path.append("./src")

import unittest
import pytest
from lib.logfile_ip_reader_v2 import LogfileIPReader


class LogfileIPReaderTestCase(unittest.TestCase):
    def setUp(self):
        self.file_name = "TestSample.log"
        #self.log_file_reader = LogfileIPReader()

    def tearDown(self):
        pass


class TestLogfileIPReader(LogfileIPReaderTestCase):
    def test_init(self):
        log_file_reader = LogfileIPReader(filename=self.file_name)
        print(self.file_name)
        assert isinstance(log_file_reader, LogfileIPReader)

    def test_read_log_file(self):
        log_file_reader = LogfileIPReader(filename=self.file_name)
        log_file_reader._read_log_file()
        #assert type(log_file_reader._log) is str

    def test_read_missing_log_file(self):
        log_file_reader = LogfileIPReader(filename=self.file_name)
        log_file_reader._read_log_file()
        #assert type(log_file_reader._log) is not str

    def test_analyse_log_file(self):
        log_file_reader = LogfileIPReader(filename=self.file_name)
        log_file_reader._read_log_file()
        log_file_reader._analyse_log_file()
        #assert type(log_file_reader._ip_addresses) is list
       
    def test_analyse_log_file_failed(self):
        log_file_reader = LogfileIPReader(filename=self.file_name)
        log_file_reader._read_log_file()
        log_file_reader._analyse_log_file()
        #assert type(log_file_reader._ip_addresses) is None

    def test_print_findings(self):
        log_file_reader = LogfileIPReader(filename=self.file_name)
        log_file_reader.run()
        #captured = capsys.readouterr()

    def test_run(self):    
        log_file_reader = LogfileIPReader(filename=self.file_name)
        log_file_reader.run()
        #assert isinstance(log_file_reader, LogfileIPReader)
        #assert type(log_file_reader._log) is str
        #assert type(log_file_reader._ip_addresses) is list
