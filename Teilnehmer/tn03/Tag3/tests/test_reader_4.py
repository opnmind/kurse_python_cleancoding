import sys
sys.path.append("/home/coder/Workspace/kurse_python_cleancoding/Teilnehmer/tn03/Tag3/LogfileIPReader")
import pytest
import reader_4
import unittest

PATH_TO_LOG_WITH_IP="tests/ipaddreses.log"

class TestReader(unittest.TestCase):
    
    def test_init(self):
        readerobject = reader_4.IpFinder(PATH_TO_LOG_WITH_IP)
        assert(readerobject.file_path == PATH_TO_LOG_WITH_IP)
        assert(readerobject.pattern_ip == r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    

    def test_init_with_pattern(self):
        readerobject = reader_4.IpFinder(PATH_TO_LOG_WITH_IP, r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}\b")
        assert(readerobject.file_path == PATH_TO_LOG_WITH_IP)
        assert(readerobject.pattern_ip == r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}\b")
    
    def test_read_log(self):
        readerobject = reader_4.IpFinder(PATH_TO_LOG_WITH_IP)
        readerobject.read_log()
        assert(len(readerobject.log_data)!= 0)
        assert(readerobject.log_data == "03/22 08:51:01 INFO   : 127.0.0.1 is my loopbackadapter")

    def test_read_log_fail(self):
        readerobject = reader_4.IpFinder("tests/does_not_exist")
        self.assertRaises(FileNotFoundError, readerobject.read_log)

    def test_find_ip_addresses(self):
        readerobject = reader_4.IpFinder(PATH_TO_LOG_WITH_IP)
        readerobject.read_log().find_ip_adresses()
        assert(len(readerobject.adresses) != 0)
        assert(readerobject.adresses[0]=="127.0.0.1")

    def test_find_no_ipadresses(self):
        readerobject = reader_4.IpFinder("tests/no_ipadresses.log")
        readerobject.read_log().find_ip_adresses()
        assert(len(readerobject.adresses) == 0)

    def test_get_ip_adresses(self):
        readerobject = reader_4.IpFinder("novalidpath")
        readerobject.adresses.append("127.0.0.1")
        assert(len(readerobject.get_ip_adresses()) == 1)
        assert(readerobject.get_ip_adresses()[0] == "127.0.0.1")

    def test_full_run(self):
        pass

    

if __name__ == '__main__':
    pass