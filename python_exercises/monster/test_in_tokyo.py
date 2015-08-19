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

    def test_is_not_in_tokyo(self):
        """return False if we're not in tokyo"""
        self.assertFalse(self.test_monster.in_tokyo())

    def test_is_in_tokyo(self):
        """check if return is true, when status is 'In Tokyo'"""
        self.test_monster.status = "In Tokyo"
        self.assertTrue(self.test_monster.in_tokyo())

if __name__ == '__main__':
    unittest.main()
