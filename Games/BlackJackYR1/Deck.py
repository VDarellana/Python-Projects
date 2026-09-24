from Card import *
import random
class Deck:
    def __init__(self,num_decks):
        self.num_decks = num_decks
        self.deck = []
        ranks = ('A',1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
        suits = ('c', 'd', 'h', 's')
        for i in self.num_decks:
            for rank in ranks:
                for suits in suits:
                    self.deck.append(f'{rank.__str__()}{suits.__str__()}')
        return
    def shuffle(self):
         return random.shuffle(self.deck)
    def draw_card(self):
        return self.deck.pop()
