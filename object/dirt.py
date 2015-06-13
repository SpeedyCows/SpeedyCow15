from object import Object
import pygame

class Dirt(Object):  # represents the water, not the game
    def __init__(self, dimension):
        """ The constructor of the class """
        super(Dirt, self).__init__(dimension)

        self.image = pygame.image.load('images/dirt.jpg')
        self.image = pygame.transform.scale(self.image, (dimension, dimension))
