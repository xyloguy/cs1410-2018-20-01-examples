import shape
import pygame


class Polygon(shape.Shape):
    def __init__(self, x, y, color, points):
        shape.Shape.__init__(self, x, y, color)
        self.points = points

    def translate(self):
        tpoints = []
        for (x, y) in self.points:
            nx = x + self.getX()
            ny = y + self.getY()
            npoint = (nx, ny)
            tpoints.append(npoint)
        return tpoints

    def draw(self, surface):
        color = self.getColor()
        pointlist = self.translate()
        pygame.draw.polygon(surface, color, pointlist)