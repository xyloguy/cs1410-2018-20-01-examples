class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    #show cards
    def show_cards(self):
        s = ''
        for card in self.cards:
            s += str(card)
            s += ' '
        return s.strip()

    def add_card(self, c):
        self.cards.append(c)
        # TODO: see if the busts

    def get_value(self):
        t = 0
        aces = []
        for c in self.cards:
            if c.is_ace():
                aces.append(c)
            else:
                t += c.blackjack_value()

        while t + (len(aces) * 11) > 21:
            a = aces.pop()
            a.make_hard()
            t += a.blackjack_value()

        for ace in aces:
            t += ace.blackjack_value()

        return t


if __name__ == '__main__':
    import card

    p = Player('Luke')
    p.add_card(card.Card('H', 1))
    p.add_card(card.Card('D', 1))
    p.add_card(card.Card('C', 7))
    #p.add_card(card.Card('D', 7))
    print(p.show_cards())
    print(p.get_value())
    print(p.show_cards())
