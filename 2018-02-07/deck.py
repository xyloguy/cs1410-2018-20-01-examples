import random

import card


class Deck:
    def __init__(self, decks):
        self.decks = decks
        self.cards = []
        self.newdeck()

    def newdeck(self):
        self.cards = []
        suits = ['D', 'S', 'H', 'C']
        for i in range(self.decks):
            for suit in suits:
                for value in range(1, 14):
                    c = card.Card(suit, value)
                    self.cards.append(c)
        self.shuffle()

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            self.newdeck()
        return self.cards.pop()

d = Deck(3)
print(len(d), d.cards)
d.shuffle()
print(len(d), d.cards)


for i in range(1000):
    print(len(d), d.deal())

print(len(d), d.cards)