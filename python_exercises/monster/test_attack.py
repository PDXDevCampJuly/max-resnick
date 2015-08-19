__author__ = 'Maxwell J. Resnick'

import unittest
from monster import Monster

class AttackTest(unittest.TestCase):

    """Test Monster Class attack function"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")

    def test_ideal_attack(self):
        """test ideal attack, won't ko"""
        self.assertEqual(5, self.test_monster.attack(5))

    def test_kod_attack(self):
        """test kod attack"""
        self.test_monster.attack(15)
        self.assertEqual("K.O.'d", self.test_monster.status)

    def test_incorrect_type_attack(self):
        """test if we prevent bad types"""
        with self.assertRaises(TypeError):
            self.test_monster.attack("some bad types")

    def test_negative_healt(self):
        """we should test for negative health catches"""
        pass

if __name__ == '__main__':
    unittest.main()
