
"""
importing all class of the game
from another files
"""
import sys, pygame
from assets.game import Game
from assets.character import Character
from assets.obstacle import Obstacle

"""
if __name__ is equivalent
as "__main__" then call
the class of Game
"""
if __name__ == "__main__":

    # Call the class of game
    ariq = Game()

    # Call the menu function
    ariq.menu()
