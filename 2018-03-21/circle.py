import shape
import pygame


class Circle(shape.Shape):
    def __init__(self, x, y, r, color):
        shape.Shape.__init__(self, x, y, color)
        self.radius = r

    def getRadius(self):
        return int(self.radius)

    def setRadius(self, r):
        self.radius = r

    def draw(self, surface):
        color = self.getColor()
        pos = (self.getX(), self.getY())
        radius = self.getRadius()
        pygame.draw.circle(surface, color, pos, radius)
