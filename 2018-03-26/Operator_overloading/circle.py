from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.get_radius() ** 2

    def get_circumference(self):
        return 2 * pi * self.get_radius()

    def __str__(self):
        return 'Circle({})'.format(self.get_radius())

    def __add__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        r3 = r1 + r2
        return Circle(r3)

    def __iadd__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        self.set_radius(r1 + r2)

    def __gt__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        return r1 > r2

    def __eq__(self, other):
        comp1 = self > other
        comp2 = other > self
        return not comp1 and not comp2

    def __lt__(self, other):
        return other > self

    def __ne__(self, other):
        return not self == other


if __name__ == '__main__':
    c1 = Circle(5)
    print(c1)
    c2 = Circle(10)
    print(c2)
    c3 = c1 + c2
    print(c3)


    print(c3 != c2)