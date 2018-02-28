import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import ball

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "EXAMPLE"
# pixels width
WINDOW_WIDTH  = 800
# pixels high
WINDOW_HEIGHT = 800
# frames per second
DESIRED_RATE  = 72

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )
        
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = ball.Ball(width, height)
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        # mouse_position contains x and y location of mouse in window
        # dt contains the number of seconds since last frame
        x = mouse_position[0]
        y = mouse_position[1]


        self.mGame.evolve( dt )
        return
    
    def paint( self, surface ):
        surface.fill((0, 0, 0))


        # Draw the current state of the game instance
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
