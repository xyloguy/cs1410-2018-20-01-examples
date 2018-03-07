from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, x, y, size, color):
        Rectangle.__init__(self, x, y, size, size, color)

    def get_size(self):
        return self.get_width()

    def set_size(self, size):
        Rectangle.set_width(self, size)
        Rectangle.set_height(self, size)

    def set_width(self, size):
        self.set_size(size)

    def set_height(self, size):
        self.set_size(size)


if __name__ == '__main__':
    s = Square(10, 20, 10, (0, 0, 0))
    print(s.x, s.y, s.color)  # 10 20 (0, 0, 0)
    print(s.get_area())  # 100
    print(s.get_perimeter())  # 40
    s.set_size(20)
    print(s.get_area())  # 400
    print(s.get_perimeter())  # 80
    s.set_size(-1)
    s.set_width(20)
    s.set_height(1)
    print(s.get_area())