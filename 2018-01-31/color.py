class Color:
    def __init__(self, r, g, b):
        self.__red = 0
        self.__green = 0
        self.__blue = 0

        self.set_red(r)
        self.set_green(g)
        self.set_blue(b)

    @property
    def red(self):
        return self.get_red()

    def get_red(self):
        return round(self.__red)

    def set_red(self, newvalue):
        if 0 <= newvalue <= 255:
            self.__red = newvalue
            return True
        return False

    def get_green(self):
        return round(self.__green)

    def set_green(self, newvalue):
        if 0 <= newvalue <= 255:
            self.__green = newvalue
            return True
        return False

    def get_blue(self):
        return round(self.__blue)

    def set_blue(self, newvalue):
        if 0 <= newvalue <= 255:
            self.__blue = newvalue
            return True
        return False

    def get_tuple(self):
        t = (self.get_red(), self.get_green(), self.get_blue())
        return t

c = Color(0.6, 2.7, 1.1)
print((c.red, c.get_green(), c.get_blue()))
print(c.get_tuple())