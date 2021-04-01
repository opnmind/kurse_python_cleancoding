import unittest
import pytest
from reader_4 import IpFinder 

class TestReader(unittest.TestCase):

    FILE_PATH_VALID = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"
    FILE_PATH_INVALID = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.lÖg"
    EMTPY_FILE_PATH_VALID = "/home/coder/Workspace/kurse_python_cleancoding/Teilnehmer/tn11/Tag3/SampleEmpty.log"

    def test_init(self):        
        finder = IpFinder(self.FILE_PATH_VALID)
        self.assertEqual(finder.file_path, self.FILE_PATH_VALID)

    def test_read_log(self):
        finder = IpFinder(self.FILE_PATH_VALID).read_log()
        self.assertIsNotNone(finder)
    
    def test_read_log_fail(self):
        try:
            finder = IpFinder(self.FILE_PATH_INVALID).read_log()
        except FileNotFoundError:
            return
        self.assertRaises(Exception("Failed test test_read_log_fail"))
    
    def test_read_log_path_override(self):
        finder = IpFinder("").read_log(self.FILE_PATH_VALID)
        if finder:
            return

    def test_read_log_path_override_fail(self):
        with self.assertRaises(FileNotFoundError):
            IpFinder("").read_log(self.FILE_PATH_INVALID)


    def test_find_ip_addresses(self):
        IpFinder("").read_log(self.FILE_PATH_VALID).find_ip_adresses()
        

    def test_find_no_ip_addresses(self):
        IpFinder("").read_log(self.EMTPY_FILE_PATH_VALID).find_ip_adresses()
                

    def test_get_ip_addresses(self):
        found = IpFinder("SampleOneIP.log").get_ip_adresses()
        self.assertEqual(len(found), 1)

    def test_full_run(self):
        pass
