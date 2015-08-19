__author__ = 'Maxwell J. Resnick'

"""A monster class for 8/19/2015"""


class Monster:

    """
    Class created based upon UML Diagram provided during class.
    """

    def __init__(self, name):
        self.name = name
        pass

    def reset(self):
        """
        resets Monster to initial stats
        :return: nothing
        """
        pass

    def in_tokyo(self):
        """
        :return: bool - True if Monster status is "In Tokyo"
        """
        pass

    def flee(self):
        """
        prompts monster to see if they want to flee Tokyo
        :return: bool True if to flee False if to stay
        """
        to_flee = input("Would you like to flee Tokyo? ").lower()
        if to_flee == "y":
            return True
        else:
            return False

    def heal(self, heal_amount):
        """
        amount to heal, up to ten.
        :param heal_amount: int
        """
        pass

    def attack(self, damage_amount):
        """
        sets status to "K.O.'d"
        :param damage_amount: int
        :return: health: int: current health amount
        """
        pass

    def score(self, points_scored):
        """
        add pass param to Monster's victory_points, and return victory pts
        :param points_scored: int: score to be added
        :return: victory_points: int: new victory points
        """
        pass