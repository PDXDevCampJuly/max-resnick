__author__ = 'Maxwell J. Resnick'

import unittest
from monster import Monster


class MonsterFleeTest(unittest.TestCase):

    """Test Monster Class flee functions"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")

    def test_flee(self):
        """tests prompt flee function"""
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
