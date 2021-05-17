import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(v) for v in range(1, 14) for j in range(4)]
        random.shuffle(self.cards)

    def deal(self):
        top_deck = self.cards.pop()
        return top_deck