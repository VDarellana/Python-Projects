from Deck import *
from Hand import *

class Game:
    def __init__(self,num_decks=1):
        self.deck = Deck(num_decks)
    def play(self):
        self.play_round()

    def play_round(self):
        _player_hand = self.Hand()
        _Computer_hand = self.Hand()
        for start in range(2):
            _player_hand.addCard()
            _Computer_hand.addCard()
        while True:
            _Player_hand.showHand()
