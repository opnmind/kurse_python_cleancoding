import unittest
import pytest
import reader_4


class TestReader(unittest.TestCase):
    def test_init(self):
        r = reader_4.IpFinder(file_path="FilePath", pattern_ip="Pattern")
        self.assertEqual(r.file_path, "FilePath")
        self.assertEqual(r.pattern_ip, "Pattern")

    def test_init_pattern(self):
        r = reader_4.IpFinder(file_path="FilePath")
        self.assertEqual(r.file_path, "FilePath")
        self.assertEqual(r.pattern_ip, reader_4.IpFinder.PATTERN_IP)

    def test_read_log(self):
        r = reader_4.IpFinder(file_path="./testData-1.log").read_log()
        self.assertNotEqual(len(r._log_data), 0)
        
    def test_get_logdata(self):
        pass

    def test_get_logdata_empty(self):
        pass
    
    def test_read_log_fail(self):
        with self.assertRaises(FileNotFoundError):
            reader_4.IpFinder("unknown").read_log()

    def test_find_ip_adresses(self):
        r = reader_4.IpFinder(file_path="./testData-1.log").read_log()
        r.find_ip_adresses()
        self.assertEqual(len(r._adresses), 3)

    def test_find_no_ipadresses(self):
        r = reader_4.IpFinder(file_path="./testData-3.log").read_log()
        r.find_ip_adresses()
        self.assertEqual(len(r._adresses), 0)

    def test_get_ip_adresses(self):
        r = reader_4.IpFinder(file_path="./testData-1.log").read_log()
        r.find_ip_adresses()
        self.assertEqual(r.get_ip_adresses(), ["127.0.0.1","192.168.100.55","10.0.0.1"])



