import pygame

class Boat:
    def __init__(self, width, height, skycolor=(0,0,0)):
        self.width = width
        self.height = height
        self.skycolor = skycolor

    def set_sky_color(self, color):
        self.skycolor = color

    def draw(self, surface):
        #boat
        pygame.draw.circle(
            surface,
            (92, 60, 8),  # brown
            (self.width//2, self.height//4),
            self.width//2
        )

        #sky
        rect = pygame.Rect(0, 0, self.width, self.height//3 * 2)
        pygame.draw.rect(surface, self.skycolor, rect)

        #mast

        #sail
