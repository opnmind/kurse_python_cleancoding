import reader
import writer
import game


#input_file = reader.FileReader("./tipp.txt")
#result_file = writer.FileWriter("./result.txt")

game.game_factory("./tipp.txt", "./result.txt").load_tipp().roll_dices().count_matches().send_results()













"""
import unittest
from unittest.mock import Mock

class Tests(unittest.TestCase):
    input_file = Mock()

    def test_valid_values(self):
        self.input_file.read.return_value = "1,2,3,4,5,6"
        game.Game().load_tipp(self.input_file)

    def test_invalid_number(self):
        self.input_file.read.return_value = "1,2,3,4,5"
        with self.assertRaises(IndexError):
            game.Game().load_tipp(self.input_file)
    
    def test_invalid_type(self):
        self.input_file.read.return_value = "1,2,3,4,5,Willi"
        with self.assertRaises(ValueError):
            game.Game().load_tipp(self.input_file)
    
    def test_doubled_number(self):
        self.input_file.read.return_value = "1,2,3,4,5,5"
        with self.assertRaises(ValueError):
            game.Game().load_tipp(self.input_file)

    def test_out_of_range_number(self):
        self.input_file.read.return_value = "1,2,3,4,5,99"
        with self.assertRaises(game.TooBigNumberError):
            game.Game().load_tipp(self.input_file)
"""