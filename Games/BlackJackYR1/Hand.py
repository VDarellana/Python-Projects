from Card import *

class Hand:
    def __init__(self):
        self.hand = []
    def addCard(self, card):
        self.hand.append(card)
        return self
    def total(self):
        total = 0
        Ace_count = 0

        for card in self.hand:
            if card.rank == 'J' or 'Q' or 'K':
                total += 10
            elif card.rank == 'A' and  Ace_count == 0:
                total += 11
                Ace_count += 1
            elif card.rank == 'A' and Ace_count >= 1:
                total += 1
            else:
                total += card.rank
        if Ace_count <= 1:
            return total
        else:
            return total-11, total
    def __str__(self):
        if self.hand == []:
            return "Empty Hand"
        else:
            return "{"+' '.join(self.hand)+"}"