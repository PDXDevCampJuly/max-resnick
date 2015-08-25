__author__ = 'Maxwell J. Resnick'

"""A monster class for 8/19/2015"""


class Monster:

    """
    Class created based upon UML Diagram provided during class.
    """

    def __init__(self, name):
        self.name = name
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def reset(self):
        """
        Resets Monster to initial stats
        Returns:
            :return: n/a
        """
        self.__init__(self.name)

    def in_tokyo(self):
        """
        Checks if the monster is within Tokyo e.g. status == "In Tokyo"
        Returns:
            :return: bool - True if Monster status is "In Tokyo"
        """
        if self.status == "In Tokyo":
            return True
        else:
            return False

    def flee(self):
        """
        Prompts monster to see if they want to flee Tokyo
        Returns:
            :return: bool True if to flee False if to stay in Tokyo
        """
        still_prompt = True
        while still_prompt:
            to_flee = input("Would you like to flee Tokyo? ").lower()
            if "y" in to_flee:
                return True
            elif "n" in to_flee:
                return False

    def heal(self, heal_amount):
        """
        Amount to heal, up to ten.
        Args:
            :param heal_amount: int
        Returns:
            :raises: Type errir if param1 isn't a int
        """

        if not type(heal_amount) == int:
            raise TypeError

        if heal_amount <= 0:
            raise ValueError
        # we use temp, so we don't have a temporary super health status.
        temp = self.health + heal_amount
        if temp >= 10:
            self.health = 10
        else:
            self.health = temp
        return self.health

    def attack(self, damage_amount):
        """
        Sets status to "K.O.'d"
        Args:
            :param damage_amount: int
        Returns:
            :return: health: int: current health amount
            :raises: Type errir if param1 isn't a int
        """

        if not type(damage_amount) == int:
            raise TypeError
        self.health -= damage_amount
        if self.health <= 0:
            self.status = "K.O.'d"
        return self.health

    def score(self, points_scored):
        """
        Add passed param to Monster's victory_points, and return victory pts
        if VP >= 20, set status to 'WINNING'
        Args:
            :param points_scored: int: score to be added
        Return:
            :return: victory_points: int: new victory points
            :raises: TypeError if param1 isn't a int
        """
        if not type(points_scored) == int:
            raise TypeError
        self.victory_points += points_scored
        if self.victory_points >= 20:
            self.status = "WINNING"
        return self.victory_points
