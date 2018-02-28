import pygame
import boat

class Picture:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height

        self.skycolor = (0, 230, 255)

        self.mBoat = boat.Boat(width, height, self.skycolor)
        #self.mBoat.set_sky_color(self.skycolor)

    # move the circles down every frame according to how much time has passed
    # don't let the circles go off the window
    def evolve(self, dt):
        return

    # draws the current state of the system
    def draw(self, surface):
        self.mBoat.draw(surface)
        return
