import os, base64, pygame, sys, random
from pygame.locals import *

"""
Make the class of character to spawn the
character's playes
"""
class Character(pygame.sprite.Sprite):

    """
    Initiating all the unit
    """
    def __init__(self, color, x, y, width, height):

        # Inheritance pygame.sprite.Sprite to make
        # sprite object
        super().__init__()

        # Set the width and the height
        self.image = pygame.Surface([width, height])

        # Set the color of the character
        self.image.fill(color)

        pygame.draw.rect(self.image, color, [x, y, width, height])

        # Get the rect's data of the character
        self.rect = self.image.get_rect()
        self.color = color
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
