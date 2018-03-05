import shape


class Rectangle(shape.Shape):
    def __init__(self, x, y, width, height, color):
        shape.Shape.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2
