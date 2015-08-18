__author__ = 'Maxwell J. Resnick'

import unittest
from angry_dice import AngryDice
from unittest.mock import patch

class ParseInputTest(unittest.TestCase):
    """Tests clean_input function of the angry_dice module"""


    def setUp(self):
        self.new_game = AngryDice(False)
        print(self.shortDescription())

    @patch('builtins.input', return_value='a')
    def test_parse_single_a(self, return_value):
        """ tests the function correctly respond with 'a' for a single 'a' roll request"""
        self.assertEqual(['a'], self.new_game.parse_input())

    @patch('builtins.input', return_value='aaaaaaaaaa')
    def test_parse_many_a(self, return_value):
        """ tests the function correctly respond with 'a' for many 'a' roll request"""
        self.assertEqual(['a'], self.new_game.parse_input())

    @patch('builtins.input', return_value='aaaaccc32423432aaaaaa')
    def test_parse_many_a_and_others(self, return_value):
        """ tests the function correctly respond with 'a' for a many 'a' + invalid roll request"""
        self.assertEqual(['a'], self.new_game.parse_input())

    @patch('builtins.input', return_value='b')
    def test_parse_single_b(self, return_value):
        """ tests the function correctly respond with 'b for a single 'b' roll request"""
        self.assertEqual(['b'], self.new_game.parse_input())

    @patch('builtins.input', return_value='bbbbbb')
    def test_parse_many_a(self, return_value):
        """ tests the function correctly respond with 'b' for many 'b' roll request"""
        self.assertEqual(['b'], self.new_game.parse_input())

    @patch('builtins.input', return_value='bbbccc32423432bbb')
    def test_parse_many_a_and_others(self, return_value):
        """ tests the function correctly respond with 'a' for a many 'a' + invalid roll request"""
        self.assertEqual(['b'], self.new_game.parse_input())

if __name__ == '__main__':
    unittest.main()
