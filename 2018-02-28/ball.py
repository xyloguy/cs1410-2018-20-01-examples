import pygame

class Ball:
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height

        self.size = 50
        self.x = width//2 - self.size//2
        self.y = height//2 - self.size//2

        self.dx = 200
        self.dy = 200

    def evolve(self, dt):
        dx = self.dx * dt
        dy = self.dy * dt

        newx = self.x + dx
        if newx <= 0 or newx + self.size >= self.screen_width:
            self.dx *= -1

        newy = self.y + dy
        if newy <= 0 or newy + self.size >= self.screen_height:
            self.dy *= -1

        self.x = newx
        self.y = newy

        return

    def draw(self, surface):
        color = (255, 0, 0)
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, color, rect)