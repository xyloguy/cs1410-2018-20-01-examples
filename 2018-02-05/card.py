class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.valuemap = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K',
        }

    def __repr__(self):
        value = self.value
        if value in self.valuemap:
            value = self.valuemap[value]
        return str(value) + self.suit