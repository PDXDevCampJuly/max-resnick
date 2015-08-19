__author__ = 'Maxwell J. Resnick'

import unittest
from monster import Monster

class InTokyoTest(unittest.TestCase):

    """Test Monster Class in_tokyo function"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")

    def test_is_in_tokyo_on_init(self):
        """check if we initialize correctly"""
        self.assertEqual("Out of Tokyo", self.test_monster.status)


if __name__ == '__main__':
    unittest.main()
