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

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
