import pygame
import game
import froggerlib
from config import *

# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE


class PygameApp(game.Game):
    def __init__(self):
        game.Game.__init__(
            self,
            'Frogger',
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            FRAME_RATE
        )

        self.stage1 = froggerlib.Stage(0, 10 * VG, SCREEN_WIDTH, VG)
        self.stage2 = froggerlib.Stage(0, 5 * VG, SCREEN_WIDTH, VG)
        self.road = froggerlib.Road(0, 6 * VG, SCREEN_WIDTH, 4 * VG)
        self.frog = None
        self.restart()

        y = 9 * VG + PADDING
        self.cars = [
            froggerlib.Car(0, y, FROG_SIZE * 2, FROG_SIZE, SCREEN_WIDTH, y, 5),
            froggerlib.Car(SCREEN_WIDTH//4 * 3, y, FROG_SIZE * 2, FROG_SIZE, SCREEN_WIDTH, y, 5),
            froggerlib.Car(SCREEN_WIDTH//4 * 2, y, FROG_SIZE * 2, FROG_SIZE, SCREEN_WIDTH, y, 5),
            froggerlib.Car(SCREEN_WIDTH//4, y, FROG_SIZE * 2, FROG_SIZE, SCREEN_WIDTH, y, 5),
        ]
        return

    def restart(self):
        x = COLS // 2 * HG + PADDING
        y = (ROWS - 1) * VG + PADDING
        self.frog = froggerlib.Frog(x, y, FROG_SIZE, FROG_SIZE, x, y, 8, HG, VG)

    def dead(self):
        if self.frog.outOfBounds(SCREEN_WIDTH, SCREEN_HEIGHT):
            return True

        # did it get hit by a car?
        for c in self.cars:
            if c.hits(self.frog):
                return True

        # did drown?

        # did hit grass?

        return False

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
        if self.dead():
            if pygame.K_r in newkeys:
                self.restart()
            return

        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_LEFT in newkeys:
            self.frog.left()

        if pygame.K_RIGHT in newkeys:
            self.frog.right()

        if pygame.K_UP in newkeys:
            self.frog.up()

        if pygame.K_DOWN in newkeys:
            self.frog.down()

        for c in self.cars:
            c.move()
            if c.atDesiredLocation():
                if c.getDesiredX() > 0:
                    c.setX(0 - c.getWidth())
                else:
                    c.setX(SCREEN_WIDTH)
        self.frog.move()

        return

    def px(self, x):
        return x * HG

    def py(self, y):
        return y * VG

    def draw_object(self, surface, obj, color):
        rect = pygame.Rect(
            obj.getX(),
            obj.getY(),
            obj.getWidth(),
            obj.getHeight()
        )
        pygame.draw.rect(surface, color, rect)

    def draw_stage(self, surface, stage):
        color = (255, 191, 250)
        self.draw_object(surface, stage, color)

    def draw_road(self, surface, road):
        color = (48, 48, 48)
        self.draw_object(surface, road, color)

    def draw_frog(self, surface):
        color = (0, 255, 0)
        self.draw_object(surface, self.frog, color)

    def draw_car(self, surface, car):
        color = (255, 0, 0)
        self.draw_object(surface, car, color)

    def draw_grid(self, surface):
        if not DEBUG:
            return

        for y in range(ROWS):
            for x in range(COLS):
                px = self.px(x)
                py = self.py(y)
                rect = pygame.Rect(px, py, HG, VG)
                pygame.draw.rect(surface, (255, 255, 0), rect, 1)


    def paint(self, surface):
        self.draw_stage(surface, self.stage1)
        self.draw_stage(surface, self.stage2)
        self.draw_road(surface, self.road)


        for c in self.cars:
            self.draw_car(surface, c)



        self.draw_frog(surface)
        self.draw_grid(surface)
        return


def main():
    pygame.font.init()
    game = PygameApp()
    game.main_loop()


if __name__ == "__main__":
    main()
