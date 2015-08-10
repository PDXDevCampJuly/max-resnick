"""
A customizable multifaced die
"""
from random import randint
from sys import argv

class Die:
    """
    A representation of a die based on customization.
    """

    def __init__(self, *args):
        # If we've never been rolled, we don't have a value.
        self.currentValue = ""
        if len(args) >= 2:
            # build dice
            self.possibleValues = args
            # storing sides as a dictionary, possibly for future use
            self.sides, self.size = self.build_sides(args)
        else:
            print("You must define more than two sides")
            raise ValueError

    def __repr__(self):
        """
        returns: current side of dice, None if it's never been rolled.
        """
        if len(self.currentValue) == 0:
            return "An unrolled die."
        elif len(self.currentValue) > 0:
            return self.currentValue

    def build_sides(self, list_of_sides):
        """
        input: list of sides to build
        return: dictionary representation of die
        """
        built_sides = {}
        for side, value in enumerate(list_of_sides):
            built_sides[side] = value
        return built_sides, len(built_sides)

    def roll(self):
        """
        return: random side of dice.
        """
        random_side = randint(0, self.size - 1)
        self.currentValue = self.sides[random_side]
if __name__ == '__main__':
    new_dice = Die(argv)
    print(new_dice.roll())
