class Square:
    def __init__(self, side):
        self.side = side

    def getSide(self):
        return self.side
    def getWidth(self):
        return self.getSide()
    def getHeight(self):
        return self.getSide()
    def getArea(self):
        return self.getSide() ** 2
    def getPerimiter(self):
        return self.getSide() * 4



s=Square(10)
print(s.getSide())
print(s.getWidth())
print(s.getHeight())
print(s.getArea())
print(s.getPerimiter())