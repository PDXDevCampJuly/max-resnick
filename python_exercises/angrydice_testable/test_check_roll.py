__author__ = 'Maxwell J. Resnick'

import unittest
from angry_dice import AngryDice


class AngryCheckRoll(unittest.TestCase):
    """Tests that AngryDie's exit stage function works"""

    def setUp(self):
        self.new_game = AngryDice(False)
        print(self.shortDescription())

    def test_stage_1_correct_exit(self):
        """We check if we correctly exit stage 1"""
        self.new_game.current_dice_a_value = 1
        self.new_game.current_dice_b_value = 2
        self.assertEqual(2, self.new_game.check_roll())

    def test_stage_2_correct_exit(self):
        """We check if we correctly exit stage 2"""
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_dice_b_value = 4
        self.new_game.current_stage = 2
        self.assertEqual(3, self.new_game.check_roll())

    def test_stage_3_correct_exit(self):
        """We check if we correctly exit stage 3"""
        self.new_game.current_dice_a_value = 5
        self.new_game.current_dice_b_value = 6
        self.new_game.current_stage = 3
        self.assertEqual(4, self.new_game.check_roll())

    def test_stage_1_incorrect_dbl_exit_cond(self):
        """We check if we correctly stop exit stage 1 w/ two invalid cond"""
        self.new_game.current_dice_a_value = 5
        self.new_game.current_dice_b_value = 6
        self.new_game.current_stage = 1
        self.assertEqual(1, self.new_game.check_roll())

    def test_stage_2_incorrect_dbl_exit_cond(self):
        """We check if we correctly stop exit stage 2 w/ two invalid cond"""
        self.new_game.current_dice_a_value = 2
        self.new_game.current_dice_b_value = 1
        self.new_game.current_stage = 2
        self.assertEqual(2, self.new_game.check_roll())

    def test_stage_3_incorrect_dbl_exit_cond(self):
        """We check if we correctly stop exiting stage 3 w/ two invalid cond"""
        self.new_game.current_dice_a_value = 1
        self.new_game.current_dice_b_value = 4
        self.new_game.current_stage = 3
        self.assertEqual(3, self.new_game.check_roll())

    def test_stage_1_incorrect_single_exit_cond(self):
        """We check if we correctly stop exit stage 1 w/ one invalid cond"""
        self.new_game.current_dice_a_value = 1
        self.new_game.current_dice_b_value = 6
        self.new_game.current_stage = 1
        self.assertEqual(1, self.new_game.check_roll())

    def test_stage_2_incorrect_single_exit_cond(self):
        """We check if we correctly stop exit stage 2 w/ one invalid cond"""
        self.new_game.current_dice_a_value = "ANGRY"
        self.new_game.current_dice_b_value = 1
        self.new_game.current_stage = 2
        self.assertEqual(2, self.new_game.check_roll())

    def test_stage_3_incorrect_single_exit_cond(self):
        """We check if we correctly stop exiting stage 3 w/ one invalid cond"""
        self.new_game.current_dice_a_value = 5
        self.new_game.current_dice_b_value = "ANGRY"
        self.new_game.current_stage = 3
        self.assertEqual(3, self.new_game.check_roll())

    def test_mutilated_stage_conditions(self):
        """We mutate stage exit conditions, and check if we still work."""
        self.new_game.STAGE = {1: [7, 8],
                               2: ['SAD', 4],
                               3: [10, 6]}
        self.new_game.current_dice_a_value = 5
        self.new_game.current_dice_b_value = "ANGRY"
        self.new_game.current_stage = 3
        self.assertEqual(3, self.new_game.check_roll())

if __name__ == '__main__':
    unittest.main()
