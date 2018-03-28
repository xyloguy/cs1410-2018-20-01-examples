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
        for i in range(1000):
            self.balls.append(ball.Ball(width, height))
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
        x = mouse_position[0]
        y = mouse_position[1]

        for b in self.balls:
            for b2 in self.balls:
                if b != b2 and b.hits(b2):
                    print('hit')
            b.move(dt)


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
