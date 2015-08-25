__author__ = 'Maxwell J. Resnick'

import unittest
from monster import Monster


class ResetTest(unittest.TestCase):

    """Test Monster Class reset function"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")
        self.test_monster.victory_points = 5
        self.test_monster.status = "waka"
        self.test_monster.victory_points = 2
        self.test_monster.reset()

    def test_health_status(self):
        """is our health 10"""
        self.assertEqual(10, self.test_monster.health)

    def test_victory_points(self):
        """victory should be 0"""
        self.assertEqual(0, self.test_monster.victory_points)

    def test_status(self):
        """status should be Out of tokyo"""
        self.assertEqual("Out of Tokyo", self.test_monster.status)

    def test_name(self):
        """our name should be boogie monster"""
        self.assertEqual("The Boogie Monster", self.test_monster.name)

if __name__ == '__main__':
    unittest.main()
