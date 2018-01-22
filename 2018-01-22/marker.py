class Marker:
    def __init__(self):
        self.color = (0, 0, 255)
        self.erasable = True
        self.capacity = 5
        self.tipsize = 0.001

    def write(self, length):
        self.capacity -= self.tipsize * abs(length)

    def show(self):
        print(self.color, self.erasable, self.capacity, self.tipsize)


redexpo1 = Marker()
redexpo1.color = (255, 0, 0)

blueexpo1 = Marker()
blueexpo2 = Marker()

bluesharpie1 = Marker()
bluesharpie1.erasable = False
bluesharpie1.tipsize = 0.001/5
bluesharpie1.capacity = 2.5

redexpo1.show()
blueexpo1.show()
bluesharpie1.show()

blueexpo1.show()
blueexpo1.write(999.7)
blueexpo1.show()


blueexpo2.show()
blueexpo2.write(75.8)
blueexpo2.show()


blueexpo1.write(0.3)
blueexpo1.show()