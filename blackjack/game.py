from player import Player
from deck import Deck

class Game:

    def __init__(self):
        self.players = []
        self.define_players()
        self.game_deck = Deck()
        self.start_game()
        self.turn_control()
        self.winner()


    def winner(self):
        """
        imput = player
        prints the hight score and winning player
        """
        winners = []
        canadate = 0
        for player in self.players:
            if player.score > canadate and player.score <= 21:
                canadate = player.score
                #if
                winners.append(player.name)


        # doesn't handle all players busted
        # doesn't handle a tie?
        for winner in winners:
            print("\tYay {} won! \(-u-)/".format(winner))

    def define_players(self):
        """
        imput num_players makes players
        returns player list
        """


        num_players = int(input("How many players are you playing with? "))
        if num_players >= 2 and num_players <= 5:
            for player in range(num_players):
                player_name = input("Please enter player {}'s name: ".format(player+1))
                self.players.append(Player(player_name))
        if num_players < 2:
            print("You need between 2-5 players. Come back when you have friends you loser")
            exit()
        else:
            print("You need between 2-5 players")
            exit()
        self.players.append(Player("Dealer", True))

    def start_game(self):
        """
        Takes a deck of cards(AKA a list of card objects) and takes a list of player objects
        """
        for player in self.players:
            cards = self.game_deck.deal(2)
            if player.is_dealer:
                cards[0].is_hidden = True
            player.new_card(cards)
            #player.print_hand()


    def turn(self):
        """
        promts user for hit or stay
        """
        hit_stay = ""
        while hit_stay != "exit":
            hit_stay = input("Would you like to 'hit' or 'stay'? ").lower()
            print("----------------------------------------")
            if hit_stay == "hit" or hit_stay == "stay" or hit_stay == "exit":
                return hit_stay
            elif hit_stay != "exit":
                print("You must choose 'hit' or 'stay' or 'exit'")



    def turn_control(self):
        """
        Player can choose between "stay", "hit" or "exit"
        """

        for player in self.players:
            print("\n")
            print("----------------------------------------")
            print("It's now {}'s turn".format(player.name))
            print("----------------------------------------")
            player.print_hand()
            choice = ""
            while choice != "stay" or choice != "exit":

                if not player.is_dealer:
                    choice = self.turn()
                else:
                    choice = player.does_dealer_hit()

                if choice == "hit":
                    card = self.game_deck.deal()
                    busted = player.new_card(card)
                    player.print_hand()
                    if busted and not player.is_dealer and player.score > 21:
                        print("\tCONGRATS YOU BUSTED!!!!!")
                        break
                    elif busted and player.score == 21:
                        print("\tBLACKJACK!!")
                        break
                elif choice == "exit":
                    print("Fine, I didn't want to play with you anyways (;_;)")
                    exit()
                elif choice == "stay":
                    break







