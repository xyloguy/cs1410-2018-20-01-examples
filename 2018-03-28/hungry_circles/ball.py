import random
import pygame
import math


class Ball:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.radius = random.randint(15, 25)
        self.x = random.randint(self.radius, self.width - self.radius)
        self.y = random.randint(self.radius, self.height - self.radius)
        red = random.randint(100, 255)
        green = random.randint(100, 255)
        blue = random.randint(100, 255)
        self.color = (red, green, blue)
        self.dx = random.randint(25, 75) * random.choice([1, -1])
        self.dy = random.randint(25, 75) * random.choice([1, -1])

    def move(self, dt):
        dx = dt * self.dx
        dy = dt * self.dy

        self.x += dx
        if self.x + self.radius >= self.width:
            self.x = self.width - self.radius
            self.dx *= -1
        elif self.x - self.radius <= 0:
            self.x = 0 + self.radius
            self.dx *= -1

        self.y += dy
        if self.y + self.radius >= self.height:
            self.y = self.height - self.radius
            self.dy *= -1
        elif self.y - self.radius <= 0:
            self.y = 0 + self.radius
            self.dy *= -1

    def hits(self, other):
        x1 = self.x
        y1 = self.y

        x2 = other.x
        y2 = other.y

        r1 = self.radius
        r2 = other.radius

        d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        d2 = r1 + r2

        return d1 <= d2



    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)