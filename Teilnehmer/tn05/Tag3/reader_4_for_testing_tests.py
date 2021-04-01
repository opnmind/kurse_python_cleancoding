import unittest
import pytest
import reader_4_for_testing

class TestReader(unittest.TestCase):



    def test_init(self):
        r = reader_4_for_testing.IpFinder(file_path="FilePath", pattern_ip="Pattern")
        self.assertEqual(r.file_path, "FilePath")
        self.assertEqual(r.pattern_ip, "Pattern")
        assert type(reader_4_for_testing.IpFinder.PATTERN_IP) is str
        pass


#bei filepath müssten beispiel dateien eingesetzt werdern
    def test_log_read(self):
        r = reader_4_for_testing.IpFinder(file_path="").read_log()

    def test_read_log_fail(self):
        with self.assertRaises(FileNotFoundError):
            reader_4_for_testing.IpFinder("unknown").read_log()

    def test_find_ip_adresses(self):
        r = reader_4_for_testing.IpFinder(file_path="").read_log()
        r.find_ip_adresses()
        self.assertEqual(len(r.adresses),0)
           
    def test_find_no_ip_adresses(self):
        r = reader_4_for_testing.IpFinder(file_path="").read_log()
        r.find_ip_adresses()
        self.assertEqual(len(r.adresses),0)

    def test_get_ip_adresses(self):
        r = reader_4_for_testing.IpFinder(file_path="").read_log()
        r.find_ip_adresses()
        self.assertEqual(r.get_ip_adresses(),["127.0.0"])
