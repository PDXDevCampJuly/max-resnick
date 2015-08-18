__author__ = 'Maxwell J. Resnick'

import unittest
from angry_dice import AngryDice

class IsCheatTest(unittest.TestCase):
    """Tests is_cheat function"""

    def setUp(self):
        self.new_game = AngryDice(False)
        print(self.shortDescription())

    def test_is_holding_a_6(self):
        """test if holding w/ 6 is caught"""
        self.new_game.current_dice_a_value = 6
        self.assertTrue(self.new_game.is_cheat(["b"]))

    def test_is_holding_a_non_stage_1_value(self):
        """test if holding a value not in the current stage 1 exit cond"""
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_stage = 1
        self.assertTrue(self.new_game.is_cheat(["b"]))

    def test_is_holding_a_with_stage_1_value(self):
        """test if holding a value in stage 1 can be held"""
        self.new_game.current_dice_a_value = 1
        self.assertFalse(self.new_game.is_cheat(["b"]))

    def test_is_holding_a_non_stage_2_value(self):
        """test if holding a value not in the current stage 2 exit cond"""
        self.new_game.current_dice_a_value = 1
        self.new_game.current_stage = 2
        self.assertTrue(self.new_game.is_cheat(["b"]))

    def test_is_holding_a_with_stage_2_value(self):
        """test if holding a value in stage 2, that can be held"""
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_stage = 2
        self.assertFalse(self.new_game.is_cheat(["b"]))

    def test_is_holding_a_non_stage_3_value(self):
        """test if holding a value not in the current stage 3 exit cond"""
        self.new_game.current_dice_a_value = 1
        self.new_game.current_stage = 3
        self.assertTrue(self.new_game.is_cheat(["b"]))

    def test_is_holding_a_with_stage_3_value(self):
        """test if holding a value for stage 3 can be held"""
        self.new_game.current_dice_a_value = 5
        self.new_game.current_stage = 3
        self.assertFalse(self.new_game.is_cheat(["b"]))

    def test_is_holding_b_6(self):
        """test if holding b w/ 6 is caught"""
        self.new_game.current_dice_b_value = 6
        self.assertTrue(self.new_game.is_cheat(["a"]))

    def test_is_holding_b_non_stage_1_value(self):
        """test if holding a value not in the current stage exit cond"""
        self.new_game.current_dice_b_value = "ANGRY"
        self.new_game.current_stage = 1
        self.assertTrue(self.new_game.is_cheat(["a"]))

    def test_is_holding_b_with_stage_1_value(self):
        """test if holding b value in stage, can be held"""
        self.new_game.current_dice_b_value = 1
        self.assertFalse(self.new_game.is_cheat(["a"]))

    def test_is_holding_b_non_stage_2_value(self):
        """test if holding b value not in the current stage 2 exit cond"""
        self.new_game.current_dice_b_value = 1
        self.new_game.current_stage = 2
        self.assertTrue(self.new_game.is_cheat(["a"]))

    def test_is_holding_b_with_stage_2_value(self):
        """test if holding b value from stage 2, can be held"""
        self.new_game.current_dice_b_value = "ANGRY"
        self.new_game.current_stage = 2
        self.assertFalse(self.new_game.is_cheat(["a"]))

    def test_is_holding_b_non_stage_3_value(self):
        """test if holding b value not in the current stage 3 exit cond"""
        self.new_game.current_dice_b_value = 1
        self.new_game.current_stage = 3
        self.assertTrue(self.new_game.is_cheat(["a"]))

    def test_is_holding_b_with_stage_3_value(self):
        """test if holding b value from stage 3, can be held"""
        self.new_game.current_dice_b_value = 5
        self.new_game.current_stage = 3
        self.assertFalse(self.new_game.is_cheat(["a"]))


if __name__ == '__main__':
    unittest.main()
