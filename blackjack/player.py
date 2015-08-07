from card import Card

class Player:

    def __init__(self, name, is_dealer=False):
        self.hand = []
        self.name = name
        self.is_dealer = is_dealer
        self.score = 0
        self.target_score = 21
        if self.is_dealer:
            target_score = 17

    def calculate_score(self):
        """
        keeps track player score
        returns total points
        """
        ace = []
        self.score = 0
        for card in self.hand:
            self.score += card.real_value
            if card.face_value == "Ace" and card.real_value == 11:
                ace.append(card)
        if ace and self.score > self.target_score:
            index_of_ace = self.hand.index(ace.pop())
            self.hand[index_of_ace].flip_ace()
            return self.calculate_score()
        if self.score > self.target_score:
            return True
        elif self.score == 21:
            return True
        else:
            return False


    def hit_stay(self):
        """
        Todo place holder for AI bot
        """
        pass

    def new_card(self, new_cards):
        """
        Adds new card to hand
        imput new card
        return hand
        """
        self.hand += new_cards
        return self.calculate_score()

    def print_hand(self):
        """
        Prints players hand
        """

        print("{}'s hand and total score is {}:\n".format(self.name, self.score))
        for card in self.hand:
            print("\t - {}".format(card), sep="\n")

    def __repr__(self):
        return self.name

    def does_dealer_hit(self):
        if self.score < 17:
            return "hit"
        else:
            return "stay"




















