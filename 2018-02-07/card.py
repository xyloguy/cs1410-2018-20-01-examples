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
        self.soft = (value == 1)

    def __str__(self):
        value = self.value
        if value in self.valuemap:
            value = self.valuemap[value]
        s = str(value) + self.suit

        if self.is_soft():
            s += '*'

        return s

    def __repr__(self):
        return str(self)

    # TODO: blackjack_value()
    def blackjack_value(self):
        if self.value == 1:
            if self.is_soft():
                return 11
            return 1

        if self.value > 10:
            return 10

        return self.value

    # TODO: soft_or_hard_ace()
    def is_soft(self):
        return self.value == 1 and self.soft

    def make_hard(self):
        if self.value == 1:
            self.soft = False

if __name__ == '__main__':
    c = Card('H', 1)
    print(c)
    print(c.is_soft())
    print(c.blackjack_value())
    c.make_hard()
    print(c)
    print(c.is_soft())
    print(c.blackjack_value())
