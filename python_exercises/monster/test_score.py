__author__ = 'Maxwell J. Resnick'

import unittest
from monster import Monster

class ScoreTEst(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
