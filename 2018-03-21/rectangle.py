import pygame
from shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, color, width, height):
        Shape.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def draw(self, surface):
        rect = pygame.Rect(
            self.getX(),
            self.getY(),
            self.getWidth(),
            self.getHeight()
        )
        pygame.draw.rect(surface, self.getColor(), rect)
