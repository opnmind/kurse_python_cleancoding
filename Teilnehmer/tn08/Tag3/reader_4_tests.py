import unittest
import pytest
import reader_4


class TestReader(unittest.TestCase):
    
    def test_init(self):
        new_reader = reader_4.IpFinder(file_path="Path", pattern_ip="my_pattern")
        assert new_reader.file_path == "Path"
        assert new_reader.pattern_ip == "my_pattern"

    def test_read_log(self):
        new_reader = reader_4.IpFinder(file_path="/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log")
        self.assertNotEqual(new_reader.log_data, [])

    def test_read_log_fail(self):
        new_reader = reader_4.IpFinder("not_here")
        with self.assertRaises(FileNotFoundError):
            new_reader.read_log()

    def test_find_ip_adresses(self):
        pass

    def test_find_no_ipadresses(self):
        pass

    def test_get_ip_adresses(self):
        pass





