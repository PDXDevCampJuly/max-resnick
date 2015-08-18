__author__ = 'Maxwell J. Resnick'
"""
Python implementation of the Angry Dice Game
"""
from die import Die


class AngryDice:
    """
    A class that represents the game Angry dice
    """
    # Class constants, that might make life easier for scope change.
    DICE_FACE_VALUES = [1, 2, "ANGRY", 4, 5, 6]
    STAGE = {1: [1, 2],
             2: ['ANGRY', 4],
             3: [5, 6]}
    WINNER_STRING = "You've won! Calm down!"

    def __init__(self, start=True):
        """
        input start:boolean defaults to True. If set to false the game will not start.
        """
        self.dice_a = Die(*self.DICE_FACE_VALUES)
        self.dice_b = Die(*self.DICE_FACE_VALUES)
        self.current_stage = 1
        self.current_dice_a_value = ""
        self.current_dice_b_value = ""
        self.game_over = False
        if start:
            self.game_controller()

    def game_instructions(self):
        """
        need to give user instructions
        need to prompt user to start
        """

        instructions = \
        ("Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\n"
        "Stage 1 you need to roll 1 & 2\n"
        "Stage 2 you need to roll ANGRY & 4\n"
        "Stage 3 you need to roll 5 & 6\n"
        "You can lock a die needed for your current stage\n"
        "and just roll the other one, but beware!\n"
        "If you ever get 2 ANGRY's at once, you have to restart to Stage 1!\n"
        "Also, you can never lock a 6! That's cheating!\n\n"
        "To roll the dice, simply input the name of the die you want to roll. Their names are a and b.\n")

        print(instructions)
        begin = True
        # we wait for exit or enter to be pressed.
        while begin:
            start = input("Press ENTER to start!")
            if start == '':
                begin = False
            elif start == 'exit':
                begin = False

    def parse_input(self):
        """
        Cleans input string, so we have upto two single die to use.
        """
        dice_to_roll = []
        input_string = input("Roll dice:")

        if "exit" in input_string:
            dice_to_roll.append("exit")
            self.game_over = True
            return dice_to_roll
        if "a" in input_string:
            dice_to_roll.append("a")
        if "b" in input_string:
            dice_to_roll.append("b")
        return dice_to_roll

    def get_roll(self):
        """
        need to ask user what dice they want to roll
        """
        still_rolling = True
        while still_rolling:
            dice_to_roll = self.parse_input()
            # we leave this is a string, for exit condition.
            if "exit" in dice_to_roll:
                # user typed exit, we throw game_over
                self.game_over = True
                return dice_to_roll
            elif len(dice_to_roll) != 0 and \
                "a" in dice_to_roll or "b" in dice_to_roll:
                still_rolling = False
        return dice_to_roll

    def print_roll(self, cheater):
        """
        input: boolean, if true, we print the cheater notice
        prints current roll, output should match:
        You rolled:
            a = [  5  ]
            b = [  ANGRY  ]
        You are in Stage #
        """
        if cheater:
            cheater = ("You're cheating! You cannot lock a 6!"
                       "You cannot win until you reroll it!\n")
        else:
            cheater = ""
        roll_text = "You rolled: \n" + "   a = [  {}  ]\n" + "   b = [  {}  ]"
        roll_turn = "\nYou are in Stage {}"
        statement = cheater + roll_text + roll_turn

        print(statement.format(self.current_dice_a_value,
                               self.current_dice_b_value, self.current_stage))

    def is_cheat(self, to_roll):
        """
        input a list of dice to roll (this should really be 1.)
        return true if user is holding on a 6, or
            attempting to hold a dice that's not part of current_stage
            exit criteria
        """
        # Just in case we get more that 1 item in our list
        for roll in to_roll:
            # check for holding 6 on a "a" dice
            if self.current_dice_a_value == 6 and roll == "b":
                return True

            # check for holding 6 on a "b" dice
            elif self.current_dice_b_value == 6 and roll == "a":
                return True

            # check for holding any value which is
            # not part of next stage criteria
            elif self.current_dice_a_value not in \
                    self.STAGE[self.current_stage] and roll == "b":
                return True

            # check for holding any value which is
            # not part of next stage criteria
            elif self.current_dice_b_value not in \
                    self.STAGE[self.current_stage] and roll == "a":
                return True

            # Hoooray we're not a cheat
            else:
                return False

    def check_roll(self):
        """
        checks current roll values
        first checks if we've reached angry status
        if we've met all conditions for the stage we move to the next stage
        """
        # we cast to sets for easy comparisons
        current_values = {self.current_dice_a_value,
                             self.current_dice_b_value}
        stage_complete_values = set(self.STAGE[self.current_stage])
        # if the two sets are equivalent, we get are returned a list of len 0
        # thusly we've met stage exit criteria.
        if len(stage_complete_values ^ current_values) == 0:
            self.current_stage += 1
            return self.current_stage
        else:
            return self.current_stage

    def check_angry(self):
        """
        Checks if user has reached Angry!
        Resets user to stage 1
        returns True if they've reached angry status
        """
        if self.current_dice_a_value == "ANGRY" and \
                self.current_dice_b_value == "ANGRY":

            self.current_stage = 1
            print("WOW, you're ANGRY!\n" + "Time to go back to Stage 1!")
            return True
        else:
            return False

    def game_controller(self):
        """
        Game controller handles the flow the game.
        This is equivalent to main()
        """
        self.game_instructions()
        while not self.game_over:
            to_roll = self.get_roll()
            attempted_cheat = False
            # check for holding on a non value allowed for stage, force roll
            if len(to_roll) != 2 and self.is_cheat(to_roll):
                attempted_cheat = True
                to_roll = ["a", "b"]
            for dice in to_roll:
                if dice == "a":
                    self.current_dice_a_value = self.dice_a.roll()
                elif dice == "b":
                    self.current_dice_b_value = self.dice_b.roll()
            if not self.check_angry():
                self.check_roll()

            if self.current_stage == 4:
                # we have a winner because we've incremented
                # the current stage beyond the game
                print(self.WINNER_STRING)
                self.game_over = True
            else:
                self.print_roll(attempted_cheat)

if __name__ == '__main__':
    new_game = AngryDice()
