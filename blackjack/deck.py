from itertools import product
from card import Card
from random import shuffle

class Deck:
    """
    Class for handling a deck of cards.

    """

    def __init__(self, num_decks=4):
        self.num_decks = num_decks
        self.cards_in_deck = self._build_deck()

         #self._build_deck()


    def deal(self, num_cards=1):
        """
        input: num_cards
        returns: list of card(s)
        """

        if num_cards > 0 and num_cards <= 2:
            cards_dealt = []
            for i in range(num_cards):
                cards_dealt.append(self.cards_in_deck[i])
                self.cards_in_deck.pop(i)
            return cards_dealt
        else:
            return "You must ask for one or two cards only. "

    def _build_deck(self):
        """
        input: calls rand.shuffle on cards
        returns: a list of cards
        """
        self.num_decks
        face_values = {"Two": 2,
                       "Three": 3,
                       "Four": 4,
                         "Five": 5,
                       "Six": 6,
                       "Seven": 7,
                       "Eight": 8,
                       "Nine": 9,
                       "Ten": 10,
                       "Jack": 10,
                       "Queen": 10,
                        "King": 10,
                        "Ace": 11}

        suit_values = ["Clubs", "Hearts", "Spades", "Diamonds"]

        #there'll be no error comment if they passed an incorrect num of list
        #Untested
        final_deck = []
        # if len(special_suit_values) == 4:
        #     suit_values += special_suit_values
        # else:
        #     suit_values += ["Clubs", "Hearts", "Spades", "Diamonds"]
        # #Let's people custumize their decks
        # if len(face_cards) == 4:
        #     face_values += face_cards
        # else:
        #     ace_cards = ["Jack",
        #                  "Queen",
        #                  "King",
        #                  "Ace"]
        #     face_values += face_cards

        for deck in range(self.num_decks):
            # Builds a single deck based on face_values and suit_values
            for card in product(face_values, suit_values):
                face_value, suit_value = card
                color = ""
                if suit_value == "Hearts" or suit_value == "Diamonds":
                    color == "Red"
                else:
                    color == "Black"
                final_deck.append(Card(face_value, face_values[face_value], suit_value, color))

        shuffle(final_deck)
        return final_deck










