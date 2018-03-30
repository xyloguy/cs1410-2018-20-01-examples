import pygame
import game
import ball

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "Hungry Balls"
# pixels width
WINDOW_WIDTH = 1024
# pixels high
WINDOW_HEIGHT = 900
# frames per second
DESIRED_RATE = 30


class PygameApp(game.Game):
    def __init__(self, title, width, height, frame_rate):
        game.Game.__init__(self, title, width, height, frame_rate)

        self.balls = []
        for i in range(50):
            self.add_ball()
        return

    def add_ball(self):
        self.balls.append(ball.Ball(self.width, self.height))

    def remove_dead_balls(self):
        for b in self.balls:
            if not b.alive:
                self.balls.remove(b)

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
        x = mouse_position[0]
        y = mouse_position[1]

        for b in self.balls:
            for b2 in self.balls:
                if b.hits(b2):
                    if b > b2:
                        b += b2
                    else:
                        b2 += b
                    #self.add_ball()
            b.move(dt)

        self.remove_dead_balls()

        return

    def paint(self, surface):
        surface.fill((0, 0, 0))
        for b in self.balls:
            b.draw(surface)
        return


def main():
    pygame.font.init()
    game = PygameApp(TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE)
    game.main_loop()


if __name__ == "__main__":
    main()
