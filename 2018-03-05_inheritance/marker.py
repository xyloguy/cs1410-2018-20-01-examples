class Marker:
    def __init__(self, color, cap, tip, erasable):
        self.color = color
        self.erasable = erasable
        self.capacity = cap
        self.tipsize = tip
        self.owner = None

    def add_owner(self, owner):
        self.owner = owner

    def write(self, length):
        self.capacity -= self.tipsize * abs(length)

    def show(self):
        print(self.color, self.erasable, self.capacity, self.tipsize)
