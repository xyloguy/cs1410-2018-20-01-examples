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

    def __str__(self):
        value = self.value
        if value in self.valuemap:
            value = self.valuemap[value]
        return str(value) + self.suit

    def __repr__(self):
        return str(self)

    # TODO: blackjack_value()
    def blackjack_value(self):
        d = {
            1: 11,
            11: 10,
            12: 10,
            13: 10,
        }
        if self.value in d:
            return d[self.value]
        return self.value

    # TODO: soft_or_hard_ace()

