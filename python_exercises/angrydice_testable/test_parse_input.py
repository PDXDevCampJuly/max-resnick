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
        """ tests the function correctly respond with 'b' for a many 'b' + invalid roll request"""
        self.assertEqual(['b'], self.new_game.parse_input())

    @patch('builtins.input', return_value='exit')
    def test_parse_single_exit(self, return_value):
        """ tests the function correctly respond with 'exit for a single 'b' roll request"""
        self.assertEqual(['exit'], self.new_game.parse_input())

    @patch('builtins.input', return_value='exitexitexit')
    def test_parse_many_exit(self, return_value):
        """ tests the function correctly respond with 'exit' for many 'exit' roll request"""
        self.assertEqual(['exit'], self.new_game.parse_input())

    @patch('builtins.input', return_value='bbbcccexitaaa')
    def test_parse_many_exit_and_others(self, return_value):
        """ tests the function correctly respond with 'exit' for a many 'ba' + invalid roll request"""
        self.assertEqual(['exit'], self.new_game.parse_input())

    @patch('builtins.input', return_value='e')
    def test_parse_invalid_request(self, return_value):
        """ tests the function correctly respond with '' for a 'invalid' roll request"""
        self.assertEqual([], self.new_game.parse_input())


    @patch('builtins.input', return_value='eyetiuoewurpoewur')
    def test_parse_invalid_requests(self, return_value):
        """ tests the function correctly respond with '' for many 'invalid' roll request"""
        self.assertEqual([], self.new_game.parse_input())

if __name__ == '__main__':
    unittest.main()
