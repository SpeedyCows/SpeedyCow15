from object import Object
import player_ant
import pygame
import random

class Sugar(Object):  # represents the water, not the game

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Sugar, self).__init__(dimension)

        self.red = 255
        self.green = 255
        self.blue = 255
        self.width = 0

        self.image = pygame.image.load('images/sugar.png')
        self.image = pygame.transform.scale(self.image, (dimension, dimension))

    def collide(self, object):
        if (type(object) is player_ant.Player_Ant):
            self.delete = True

    def isMovable(self):
        return False
