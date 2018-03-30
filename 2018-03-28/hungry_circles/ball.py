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
        self.alive = True

    def get_area(self):
        return math.pi * self.radius ** 2

    def set_radius_from_area(self, new_area):
        old_area = self.get_area()
        self.radius = int(math.sqrt(new_area / math.pi))

        r = new_area/old_area / 1.3
        self.dx *= r
        self.dy *= r

    def move(self, dt):
        if not self.alive:
            return

        dx = dt * self.dx
        dy = dt * self.dy

        bounce = False

        self.x += dx
        if self.x + self.radius >= self.width:
            self.x = self.width - self.radius
            self.dx *= -1
            bounce = True
        elif self.x - self.radius <= 0:
            self.x = 0 + self.radius
            self.dx *= -1
            bounce = True


        self.y += dy
        if self.y + self.radius >= self.height:
            self.y = self.height - self.radius
            self.dy *= -1
            bounce = True

        elif self.y - self.radius <= 0:
            self.y = 0 + self.radius
            self.dy *= -1
            bounce = True

        if bounce:
            if self.radius >= 30:
                new_area = self.get_area() * 0.8
                self.set_radius_from_area(new_area)

    def hits(self, other):
        # don't compare the ball against itself.
        if self is other:
            return False

        if not self.alive or not other.alive:
            return False

        # ball 1
        x1 = self.x
        y1 = self.y
        r1 = self.radius

        # ball 2
        x2 = other.x
        y2 = other.y
        r2 = other.radius

        actual_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        minimum_distance = r1 + r2

        # if the actual distance is less than the
        # the radius of ball one and the radius
        # of ball two, then they are touching or
        # overlapping so a collision has occurred.
        return actual_distance <= minimum_distance

    def draw(self, surface):
        if not self.alive:
            return
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __iadd__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        total_area = a1 + a2

        r1, g1, b1 = self.color
        r2, g2, b2 = other.color

        red = (r1 + r2) // 2
        green = (g1 + g2) // 2
        blue = (b1 + b2) // 2

        self.color = (red, green, blue)

        self.set_radius_from_area(total_area)
        other.alive = False
        return self
