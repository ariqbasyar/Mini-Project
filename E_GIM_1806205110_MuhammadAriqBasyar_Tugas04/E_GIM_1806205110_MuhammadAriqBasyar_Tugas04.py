
"""
importing all class of the game
from another files
"""
import sys
sys.path.append("../")
import pygame
from assets.game import Game
from assets.character import Character
from assets.obstacle import Obstacle
from assets.obstacle_2 import Obstacle

"""
if __name__ is equivalent
as "__main__" then call
all the class of Game
"""
if __name__ == "__main__":
    ariq = Game()

    # Call the menu function
    ariq.menu()
