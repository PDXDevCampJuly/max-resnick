class Card:
    """
    Class of cards
    """

    def __init__(self, face_value, real_value, suit, color, is_hidden=False):
    #    self.face_value_and_real_value, self.real_value = _unpack_card(face_value_and_real_value)
        self.suit = suit
        self.color = color
        self.is_hidden = is_hidden
        self.real_value = real_value
        self.face_value = face_value


    def __repr__(self):
        if self.is_hidden:
            pretty_card = "This card is hidden"
        else:
            pretty_card = str(self.face_value) + " of " + str(self.suit)
        return pretty_card

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

