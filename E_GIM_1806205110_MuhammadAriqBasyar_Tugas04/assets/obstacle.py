import os, base64, pygame, sys, random
from pygame.locals import *

"""
Make the class of obstacle to spawn an Obstacle
to the game
"""
class Obstacle(pygame.sprite.Sprite):
    """
    Initiating all the important units
    """
    def __init__(self, color, x, y, width, height):

        # Inheritance pygame.sprite.Sprite
        super().__init__()


        # Get all the data of rectangle object
        self.rect = Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.color = color

        # Make a surface object
        self.image = pygame.Surface([self.rect.width, self.rect.height])

        # Filling an obstacle with color
        self.image.fill(self.color)

        # Draw the obstacle right on the x and y
        pygame.draw.rect(self.image,
                        self.color,
                        [self.rect.x,
                        self.rect.y,
                        self.rect.width,
                        self.rect.height])


    """
    Defining a function to move the obstacle
    toward to the player's character
    """
    def update(self):

        # Moving the object with decreasing the value of x
        self.rect.x -= 2

        # If the obstacle is passed out through the screen
        if self.rect.x <= -self.rect.width:
            self.color = (random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255))
            self.rect.y = random.choice([470, 430, 390])
            self.rect.x = 800

    """
    Defining a alpha of a surface to make the
    transparency of an image/obstacle
    """
    def set_alpha(self, value):
        self.image.set_alpha(value)
