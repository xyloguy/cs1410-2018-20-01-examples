class Rectangle:
    def __init__(self, w, h):
        self.__width = w
        self.__height = h

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        w = 2 * self.getWidth()
        h = 2 * self.getHeight()
        return w + h


r = Rectangle(100, 20)
print(r.getArea()) # 2000
print(r.getPerimeter()) # 240
print(r.getWidth()) # 100
print(r.getHeight()) # 20
