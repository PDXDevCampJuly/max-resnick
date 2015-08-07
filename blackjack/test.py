from game import Game
from deck import Deck
from card import Card
from player import Player

def run_test_deck():
    test_deck = Deck()
    print(test_deck.deal())
    print(test_deck.deal(2))

def run_test_player():
    test_player = Player("John")
    print(test_player)
    return test_player

def run_test_game():
    new_game = Game()
    players_for_test = []
    players_for_test.append(Player("John"))
    players_for_test.append(Player("Sherlock"))
    new_game.players = players_for_test
    new_game.start_game()

def run_ui():
    new_game = Game()
    players_for_test = []
    players_for_test.append(Player("John"))
    players_for_test.append(Player("Sherlock"))
    new_game.players = players_for_test
    return new_game


def run_test_card():
    test_player = run_test_player()
    deck = Deck()
    test_ace = deck.cards_in_deck[deck.cards_in_deck.index("Ace")]
    test_eight = deck.cards_in_deck[deck.cards_in_deck.index("Eight")]
    test_seven = deck.cards_in_deck[deck.cards_in_deck.index("Seven")]
    print(test_player.new_card([test_ace, test_eight]))
    print(test_player.new_card([test_seven]))





