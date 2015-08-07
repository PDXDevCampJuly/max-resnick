class Card:
    """
    Class of cards
    """

    def __init__(self, face_value, real_value, suit, color):
        self.suit = suit
        self.color = color
        self.is_hidden = True
        self.real_value = real_value
        self.face_value = face_value


    def __repr__(self):
        return self.string

    def __str__(self):
        if self.is_hidden:
            pretty_card = "This card is hidden"
        else:
            pretty_card = str(self.face_value) + " of " + str(self.suit)
        return pretty_card



    def cheat(self, face_value):
        """
        TODO cheats and changes value.
        """
        pass

    def flip_ace(self):
        """
        Flips ace value to 1 or 11
        """
        if self.real_value == 1:
            self.real_value = 11
        elif self.real_value == 11:
            self.real_value = 1

