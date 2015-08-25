__author__ = 'Maxwell J. Resnick'

import unittest
from unittest.mock import patch
from monster import Monster


class MonsterFleeTest(unittest.TestCase):

    """Test Monster Class flee functions"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")

    @patch('builtins.input', return_value='y')
    def test_want_to_flee_ideal_yes(self, input_patch):
        """tests prompt flee function, we want to flee"""
        self.assertTrue(self.test_monster.flee())

    @patch('builtins.input', return_value='n')
    def test_want_to_flee_ideal_no(self, input_patch):
        """tests prompt flee function, we don't want to flee"""
        self.assertFalse(self.test_monster.flee())

    @patch('builtins.input', return_value="yy")
    def test_want_to_flee_multiple_ideal_yes(self, input_patch):
        """tests prompt flee function, but we enter multiple ideal inputs to flee"""
        self.assertTrue(self.test_monster.flee())

    @patch('builtins.input', return_value="nn")
    def test_want_to_flee_multiple_ideal_no(self, input_patch):
        """tests prompt flee function, but we enter multiple ideal inputs to flee"""
        self.assertFalse(self.test_monster.flee())

    @patch('builtins.input', side_effect=["waka", "stuffs", "y"])
    def test_want_to_flee_bad_yes(self, input_patch):
        """tests prompt flee function, but we enter multiple bad inputs to flee but do flee"""
        self.assertTrue(self.test_monster.flee())

    @patch('builtins.input', side_effect=["sasha", "zipp", "n"])
    def test_want_to_flee_bad_no(self, input_patch):
        """tests prompt flee function, but we enter multiple bad inputs to flee, but don't flee"""
        self.assertFalse(self.test_monster.flee())

if __name__ == '__main__':
    unittest.main()
