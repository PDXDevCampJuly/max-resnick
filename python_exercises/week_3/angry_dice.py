"""
Python implementation of the Angry Dice program
"""

from die import Die

# each roll need to determine if they have two angry dice, if yes restart to stage 1

# each roll need to determine if they passed stage

# each roll determine a if they have completed the game

# each roll do not allow a 6 to be held, do not allow win

class AngryDice:
    """
    A class that represents the game Angry dice
    """
    DICE_FACE_VALUES = [1, 2, "ANGRY", 4, 5, 6 ]
    STAGE = {"stage_1": [1, 2],
             "stage_2": [2, 'ANGRY'],
             "stage_3": [5]}
    def __init__(self):
        self.dice_a = Die(*self.DICE_FACE_VALUES)
        self.dice_b = Die(*self.DICE_FACE_VALUES)
        self.current_stage = "stage_1"
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
        while still_rolling:
            dirty_dice_to_roll = list(input("Roll dice:"))
            if len(dirty_dice_to_roll) != 0 and ("a" in dirty_dice_to_roll or "b" in dirty_dice_to_roll):
                still_rolling = False
            elif 'exit' in dice_to_roll:
                exit()
        if "a" in dirty_dice_to_roll:
            dice_to_roll.append("a")
        if "b" in dirty_dice_to_roll:
            dice_to_roll.append("b")
        return dice_to_roll

    def print_roll(self):
        """
        prints current roll, output should match:
        You rolled:
            a = [  5  ]
            b = [  ANGRY  ]
        """
        roll_text = "You rolled: \n" + "   a = [  {}  ]\n" + "   b = [  {}  ]"
        # TODO handle real rolls
        # TODO maybe take pre and post roll text
        print(roll_text.format(arg1, arg2))


    def ischeat(self):
        if self.current_dice_a_value == 6 or self.current_dice_b_value == 6:
            return True
        else:
            return False

    def game_controller(self):
        """
        Game controller handles the flow the game.
        """
        dice_value = []
        to_roll = self.get_roll()

        # check for holding on a 6
        if to_roll != 2 and self.ischeat():
            attempted_cheat = True
            to_roll = ["a", "b"]

        # roll the dice
        for dice in to_roll:
            if dice == "a":
                self.current_dice_a_value = self.dice_a.roll()
            elif dice == "b":
                self.current_dice_b_value = self.dice_b.roll()

        print(self.current_dice_a_value, self.current_dice_b_value)
