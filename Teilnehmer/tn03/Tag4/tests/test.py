import unittest
import pytest
from pathlib import Path
import os


@pytest.fixture
def db():
    yield DBClient()
    DBClient().close()

@pytest.fixture(scope="module")
def test_unpack_tgz_teardown(db):
    """
        Tear down function to remove testfile.txt after run
    """
    yield None
    os.remove("testfile.txt")

def test_unpack_tgz(x):
    """
    Tests the unpacking.
    """
    #creates testfile.txt for test
    
    with open("testfile.txt","w") as file:
        file.write("test")
    with open("testfile2.txt","w") as file:
        file.write("test")
    
    #checks if file exist 
    assert Path("testfile.txt").is_file() == True
    #_ = test_unpack_tgz_teardown

def test_dummy():
    assert 1 == 1
