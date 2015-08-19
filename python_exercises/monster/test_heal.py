__author__ = 'Maxwell J. Resnick'

import unittest

from monster import Monster


class HealTest(unittest.TestCase):

    """Test Monster Class heal function"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")

    def test_init_heal_value(self):
        """test initialized health value"""
        self.assertEqual(10, self.test_monster.health)

    def test_ideal_add_health(self):
        """test adding health, with input that will keep at 10 and below"""
        # we have an unhealthy monster
        self.test_monster.health = 2
        self.assertEqual(10, self.test_monster.heal(8))

    def test_ideal_too_much_health(self):
        """test adding too much health, with input that will keep at 10 and below"""
        # we have an unhealthy monster
        self.test_monster.health = 8
        self.assertEqual(10, self.test_monster.heal(8))

    def test_invalid_input_type(self):
        """test trying to add a bad type."""
        with self.assertRaises(TypeError):
            self.test_monster.heal("something")

    def test_negative_heal(self):
        """we should test for negative health catches"""
        with self.assertRaises(ValueError):
            self.test_monster.heal(-10)

if __name__ == '__main__':
    unittest.main()
