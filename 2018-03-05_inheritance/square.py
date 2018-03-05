import rectangle


class Square(rectangle.Rectangle):
    def __init__(self, x, y, size, color):
        rectangle.Rectangle.__init__(self, x, y, size, size, color)

    def get_size(self):
        return self.get_width()

    def set_size(self, size):
        self.set_width(size)
        self.set_height(size)


if __name__ == '__main__':
    s = Square(10, 20, 10, (0, 0, 0))
    print(s.x, s.y, s.color)  # 10 20 (0, 0, 0)
    print(s.get_area())  # 100
    print(s.get_perimeter())  # 40