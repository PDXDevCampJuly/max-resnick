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
    def test_want_to_flee_ideal(self, input_patch):
        """tests prompt flee function, we want to flee"""
        self.assertTrue(self.test_monster.flee())

    @patch('builtins.input', return_value='n')
    def test_want_to_flee_ideal(self, input_patch):
        """tests prompt flee function, we don't want to flee"""
        self.assertFalse(self.test_monster.flee())

if __name__ == '__main__':
    unittest.main()
