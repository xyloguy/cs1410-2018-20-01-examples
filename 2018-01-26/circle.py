import math

class Circle:
    def __init__(self):
        self.__radius = None

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = abs(radius)

    def get_diameter(self):
        r = self.get_radius()
        if r is not None:
            return r * 2
        return None

    def get_area(self):
        r = self.get_radius()
        if r is not None:
            return math.pi * r ** 2
        return None

    def get_circumference(self):
        r = self.get_radius()
        if r is not None:
            return self.get_diameter() * math.pi
        return None

c = Circle()
print(c.get_radius()) # 10
c.set_radius(-20)
print(c.get_diameter()) # 20
print(c.get_area()) # 314.2
print(c.get_circumference()) # 62.8