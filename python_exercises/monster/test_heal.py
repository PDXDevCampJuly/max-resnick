__author__ = 'Maxwell J. Resnick'

import unittest

from monster import Monster
class MyTestCase(unittest.TestCase):

    """Test Monster Class heal function"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")

    def test_init_heal_value(self):
        """test initialized health value"""
        self.assertEqual(10, self.test_monster.health)

if __name__ == '__main__':
    unittest.main()
