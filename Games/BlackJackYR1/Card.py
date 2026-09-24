class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def __str__(self):
        if self.rank.isdigit():
            return self.suit,self.rank.upper()
        else:
            return self.suit.upper(),self.rank.upper()
    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit