from object import Object
import pygame

class Water(Object):  # represents the water, not the game
    def __init__(self, dimension):
        """ The constructor of the class """
        super(Water, self).__init__(dimension)

        self.image = pygame.image.load('images/water.jpeg')
        self.image = pygame.transform.scale(self.image, (dimension, dimension))
