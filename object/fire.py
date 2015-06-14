from object import Object
from water import Water
import pygame, random, pyganim

 
class Fire(Object):  # represents the water, not the game

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Fire, self).__init__(dimension)
        
        ani_F1 = pygame.image.load('images/fire/sprite_1.png')
        ani_F2 = pygame.image.load('images/fire/sprite_2.png')
        ani_F3 = pygame.image.load('images/fire/sprite_3.png')
        ani_F4 = pygame.image.load('images/fire/sprite_4.png')
        ani_F5 = pygame.image.load('images/fire/sprite_5.png')
        self.ani_F = pyganim.PygAnimation([(ani_F1, .1), (ani_F2, .1), (ani_F3, .1), (ani_F4, .1), (ani_F5, .1)])
        self.ani_F.scale((self.dimension, self.dimension))

        # start all animations
        self.ani_conduct = pyganim.PygConductor([self.ani_F])
        self.ani_conduct.play()

        # initial animation direction to draw
        self.ani = self.ani_F

        
        self.red = 0
        self.green = 255
        self.blue = 0
        self.width = 1
        
    def collide(self, object):
        if type(object) is Water:
            self.delete = True
        
