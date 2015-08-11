"""
Python implementation of the Angry Dice program
"""

from die import Die


class AngryDice:
    """
    A class that represents the game Angry dice
    """
    DICE_FACE_VALUES = [1, 2, "ANGRY", 4, 5, 6 ]
    STAGE = {1: [1, 2],
             2: ['ANGRY', 4],
             3: [5, 6]}
    WINNER_STRING = "You've won! Calm down!"
    def __init__(self):
        self.dice_a = Die(*self.DICE_FACE_VALUES)
        self.dice_b = Die(*self.DICE_FACE_VALUES)
        self.current_stage = 1
        self.current_dice_a_value = ""
        self.current_dice_b_value = ""

    def game_instructions(self):
        """
        need to give user instructions
        need to prompt user to start
        TOOD maybe refactor so this just takes a prompt string + validator function
            returns true or false
        """

        instructions = \
        ("Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\n"
        "Stage 1 you need to roll 1 & 2\n"
        "Stage 2 you need to roll ANGRY & 4\n"
        "Stage 3 you need to roll 5 & 6\n"
        "You can lock a die needed for your current stage and just roll the other one, but beware!\n"
        "If you ever get 2 ANGRY's at once, you have to restart to Stage 1!\n"
        "Also, you can never lock a 6! That's cheating!\n\n"
        "To roll the dice, simply input the name of the die you want to roll. Their names are a and b.")

        print(instructions)
        begin = True
        # we wait for exit or enter to be pressed.
        while begin:
            start = input("waiting to begin....")
            if start == '':
                begin = False
            elif start == 'exit':
                begin = False
        print("hoozah here we go.")

    def get_roll(self):
        """
        required prompt "Roll dice:"
        need to ask user what dice they want to roll
        """
        dice_to_roll = []
        still_rolling = True
        # Used for exiting up a while stack.
        game_over = False
        while still_rolling:
            dirty_dice_to_roll = list(input("Roll dice:"))
            if len(dirty_dice_to_roll) != 0 and ("a" in dirty_dice_to_roll or "b" in dirty_dice_to_roll):
                still_rolling = False
            elif 'exit' in dice_to_roll:
                game_over = True
        if "a" in dirty_dice_to_roll:
            dice_to_roll.append("a")
        if "b" in dirty_dice_to_roll:
            dice_to_roll.append("b")
        return dice_to_roll, game_over

    def print_roll(self, cheater):
        """
        prints current roll, output should match:
        You rolled:
            a = [  5  ]
            b = [  ANGRY  ]
        """
        if cheater:
            cheater = "You're cheating! You cannot lock a 6! You cannot win until you reroll it!\n"
        else:
            cheater = ""
        roll_text = "You rolled: \n" + "   a = [  {}  ]\n" + "   b = [  {}  ]"
        roll_turn = "\nYou are in Stage {}"
        statement = cheater + roll_text + roll_turn

        # TODO maybe take pre and post roll text
        print(statement.format(self.current_dice_a_value, self.current_dice_b_value, self.current_stage))


    def ischeat(self, to_roll):
        """
        input a list of dice to roll (this should really be 1.)
        return true if user is holding on a 6
        """
        # Just in case we get more that 1 item in our list, which we shouldn't...
        for roll in to_roll:
            if self.current_dice_a_value == 6 and roll == "b":
                cheat = True
            elif self.current_dice_b_value == 6 and roll == "a":
                cheat = True
            else:
                cheat = False
        return cheat

    def check_roll(self):
        """
        checks current roll values
        first checks if we've reached angry status
        if we've met all conditions for the stage we move to the next stage
        """
        # we cast to sets for easy comparisons
        current_values = set([self.current_dice_a_value, self.current_dice_b_value])
        stage_complete_values = set(self.STAGE[self.current_stage])
        if self.check_angry():
            pass

        elif len(stage_complete_values ^ current_values) == 0:
            self.current_stage += 1

    def check_angry(self):
        """
        Checks if user has reached Angry!
        Resets user to stage 1
        returns True if they've reached angry status
        """
        if self.current_dice_a_value == "ANGRY" and self.current_dice_b_value == "ANGRY":
            self.current_stage = 1
            return True
        else:
            return False

    def game_controller(self):
        """
        Game controller handles the flow the game.
        """
        game_over = False
        while not game_over:
            to_roll, game_over = self.get_roll()
            attempted_cheat = False
            # check for holding on a 6, force roll
            if len(to_roll) != 2 and self.ischeat(to_roll):
                attempted_cheat = True
                to_roll = ["a", "b"]

            # roll the dice, cast to string, Die class can return various type.
            for dice in to_roll:
                if dice == "a":
                    self.current_dice_a_value = self.dice_a.roll()
                elif dice == "b":
                    self.current_dice_b_value = self.dice_b.roll()
            self.check_roll()
            if self.current_stage == 4:
                # we have a winner because we've incremented the current stage beyond the game
                print(self.WINNER_STRING)
                game_over = True
            else:
                self.print_roll(attempted_cheat)
