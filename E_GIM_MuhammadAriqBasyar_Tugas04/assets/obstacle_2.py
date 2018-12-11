import os, base64, pygame, sys, random
from pygame.locals import *

"""
Make the class of obstacle to spawn an Obstacle
to the game
"""
class Obstacle(pygame.sprite.Sprite):
    """
    Initiating all the unit that is impportant
    """
    def __init__(self, color, x, y, width, height):

        # Inheritance pygame.sprite.Sprite
        super().__init__()

        # Make a surface object
        self.image = pygame.Surface([width, height])

        # Filling an obstacle with color
        self.image.fill(color)

        # Draw the obstacle right on the x and y
        pygame.draw.rect(self.image, color, [x, y, width, height])

        # Get all the data of rectangle object
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

    """
    Defining a function to move the obstacle
    toward to the player's character
    """
    def update(self):

        # Moving the object with decreasing the value of x
        self.rect.x -= 3

        # Make the obstacle cycling over the screen if the obstacle is
        # passing out the screen
        if self.rect.x <= -self.rect.width:
            self.rect.x = 800
