import reader_4
import unittest
import pytest

class TestReader(unittest.TestCase):

    def test_init(self):
        myIpFinder = reader_4.IpFinder("","")
        assert myIpFinder.file_path is not None
        assert myIpFinder.adresses is not None 
        assert myIpFinder.log_data is not None
        assert myIpFinder.pattern_ip is not None
        
    def test_log_read(self):
        myIpFinder = reader_4.IpFinder("/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log","")
        assert myIpFinder.read_log() is not None
        #das 
        #self.assertEqual(len(myIpFinder._log_data) != 0)

    def test_readlog_fail(self):
        pass
    
    def test_find_ip_addresses(self):
        myIpFinder = reader_4.IpFinder("/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log","")
        myIps = myIpFinder.find_ip_adresses()
        assert myIps is not None

    def test_find_ip_addresses_fail(self):
        pass

    def test_get_ip_addresses(self):
        myIpFinder = reader_4.IpFinder("/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log","")
        assert myIpFinder.get_ip_adresses() is not None

    def test_full_run(self):
        myIpFinder = reader_4.IpFinder("/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log","")
        assert myIpFinder.read_log() is not None
        assert myIpFinder.find_ip_adresses() is not None
        assert myIpFinder.get_ip_adresses() is not None
