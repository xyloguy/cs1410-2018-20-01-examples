import pygame

class Picture:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height

    # move the circles down every frame according to how much time has passed
    # don't let the circles go off the window
    def evolve(self, dt):
        return

    # draws the current state of the system
    def draw(self, surface):
        # rectangle to fill the background
        rect = pygame.Rect(int(0), int(0), int(self.mWidth), int(self.mHeight))
        # filled rectangle
        pygame.draw.rect(surface, (255, 255, 255), rect, 0)
        #stroke
        pygame.draw.rect(surface, (0, 0, 0), rect, 20)

        startx = self.mWidth//2
        starty = self.mHeight//2
        size = 100
        pointlist = [
            (startx, starty),
            (startx - size, starty + size),
            (startx + size, starty + size)
        ]
        pygame.draw.polygon(surface,(255,255,0), pointlist)



        pygame.draw.circle(surface, (255,0,0), (startx, starty), 50)

