class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def getColor(self):
        return self.color

    def getX(self):
        return int(self.x)

    def getY(self):
        return int(self.y)

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def draw(self, surface):
        raise NotImplementedError('Must be implemented in a child class')
