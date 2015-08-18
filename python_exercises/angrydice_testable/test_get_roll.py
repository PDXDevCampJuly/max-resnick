__author__ = 'Maxwell J. Resnick'

import unittest
from angry_dice import AngryDice
from unittest.mock import patch


class GetRollTest(unittest.TestCase):
    """Test get_roll for exit conditions, and a proper list of die to roll"""

    def setUp(self):
        self.new_game = AngryDice(False)
        print(self.shortDescription())

    @patch('builtins.input', return_value="exit")
    def test_exit_condition(self, mock_input):
        """when given 'exit' input we expect game_over to be true"""
        self.assertEqual(['exit'], self.new_game.get_roll())
        self.assertTrue(self.new_game.game_over)

    @patch('builtins.input', return_value="a")
    def test_a_condition(self, mock_input):
        """when given 'a' input we expect to be given a list ['a']"""
        self.assertEqual(['a'], self.new_game.get_roll())

    @patch('builtins.input', return_value="b")
    def test_b_condition(self, mock_input):
        """when given 'b' input we expect to be given a list ['b']"""
        self.assertEqual(['b'], self.new_game.get_roll())

    @patch('builtins.input', return_value="ba")
    def test_ab_condition(self, mock_input):
        """when given 'ba' input we expect to be given a list ['b', 'a']"""
        self.assertEqual(['a', 'b'], self.new_game.get_roll())

    @patch('builtins.input', side_effect=["sdf", "wii", "stuff", "", "a"])
    def test_invalid_condition(self, mock_input):
        """when given a bad input we expect to be prompted for an input until we provide valid"""
        self.assertEqual(['a'], self.new_game.get_roll())


if __name__ == '__main__':
    unittest.main()
