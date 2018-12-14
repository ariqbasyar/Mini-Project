"""
Importing the libraries
"""
import sys, pygame
from pygame.locals import *

"""
Make the function of main and try to open the files
"""
def main():
    try:
        from assets.game import Game
        from assets.character import Character
        from assets.obstacle import Obstacle
        # Call the class of game
        ariq = Game()

        # Call the menu function
        ariq.menu()

    # Except the files are doesn't exist
    except Exception:
        pygame.font.init()
        def make_text(message, textSize, textColor):
            newFont = pygame.font.Font(None, textSize)
            newText = newFont.render(message, 0, textColor)
            return newText

        lst = ["sorry, we have an issue",
        "maybe some files are corrupted or doesn't exist",
        "please make sure you are download from:",
        "github.com/ariqbasyar/Mini-Project"]

        screen = pygame.display.set_mode((800,
        600))
        while True:
            # Filling the screen with black color
            screen.fill((0, 0, 0))

            y = 180
            for i in lst:
                isi_error_session = make_text(i,
                48, (128, 128, 128))
                isi_rect = isi_error_session.get_rect()
                screen.blit(isi_error_session,
                (400 - (isi_rect[2]/2), y))
                y += 40

            pygame.display.update()
            for event in pygame.event.get():

                # If the user is clicked at the button of exit
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

"""
if __name__ is equivalent
as "__main__" then call
the main function
"""
if __name__ == "__main__":
    main()
