__author__ = 'Maxwell J. Resnick'

import unittest
from monster import Monster

class ScoreTest(unittest.TestCase):

    """Test Monster Class score function"""

    def setUp(self):
        print(self.shortDescription())
        self.test_monster = Monster("The Boogie Monster")

    def test_score_init(self):
        """make sure score is initialized."""
        self.assertEqual(0, self.test_monster.victory_points)

    def test_score_ideal(self):
        """make sure score is added."""
        self.assertEqual(5, self.test_monster.score(5))

    def test_winning_score_is_20(self):
        """make sure we set the status to winning if vp equal 20"""
        self.test_monster.score(20)
        self.assertEqual("WINNING", self.test_monster.status)

    def test_winning_score_is_over_20(self):
        """make sure we set the status to winning if vp equal to or exceeds 20"""
        self.test_monster.score(25)
        self.assertEqual("WINNING", self.test_monster.status)

    def test_make_sure_status_doesnt_chage(self):
        """ make sure we aren't greedy with winning status"""
        self.test_monster.score(5)
        self.assertNotEqual("WINNING", self.test_monster.status)

    def test_type_checking(self):
        """ can we handle types!"""
        with self.assertRaises(TypeError):
            self.test_monster.heal("something")
if __name__ == '__main__':
    unittest.main()
