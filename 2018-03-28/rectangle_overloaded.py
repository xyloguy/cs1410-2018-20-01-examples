class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return self.get_width() * 2 + self.get_height() * 2

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return other > self

    def __eq__(self, other):
        # return self.get_area() == other.get_area()
        return not self > other and not self < other

    def __add__(self, other):
        total_area = self.get_area() + other.get_area()
        n = total_area / (self.get_width() + self.get_height())
        nw = n * self.get_width()
        nh = n * self.get_height()
        return Rectangle(nw, nh)

    def __mul__(self, other):
        nw = self.get_width() + other.get_width()
        nh = self.get_height() + other.get_width()
        return Rectangle(nw, nh)

    def __iadd__(self, other):
        r3 = self + other
        self.set_width(r3.get_width())
        self.set_height(r3.get_height())
        return self


if __name__ == "__main__":
    r1 = Rectangle(20, 10)
    r2 = Rectangle(5, 30)
    r3 = r1 + r2
    r4 = r1 + r2 + r3
    r1 += r2

    print(r3.get_width(), r3.get_height())
    print(r1.get_width(), r1.get_height())
    print(350/3*2, 350/3)



