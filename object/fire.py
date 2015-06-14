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
        self.ani_F = pyganim.PygAnimation([(ani_F1, 0.1), (ani_F2, 0.1), (ani_F3, 0.1), (ani_F4, 0.1), (ani_F5, 0.1)])
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
        
    def explode(self):
        ani_E1 = pygame.image.load('images/explosion/sprite_1.png')
        ani_E2 = pygame.image.load('images/explosion/sprite_2.png')
        ani_E3 = pygame.image.load('images/explosion/sprite_3.png')
        ani_E4 = pygame.image.load('images/explosion/sprite_4.png')
        ani_E5 = pygame.image.load('images/explosion/sprite_5.png')
        ani_E6 = pygame.image.load('images/explosion/sprite_6.png')
        ani_E7 = pygame.image.load('images/explosion/sprite_7.png')
        ani_E8 = pygame.image.load('images/explosion/sprite_8.png')
        ani_E9 = pygame.image.load('images/explosion/sprite_9.png')
        ani_E10 = pygame.image.load('images/explosion/sprite_10.png')
        ani_E11 = pygame.image.load('images/explosion/sprite_11.png')
        ani_E12 = pygame.image.load('images/explosion/sprite_12.png')
        ani_E13 = pygame.image.load('images/explosion/sprite_13.png')
        ani_E14 = pygame.image.load('images/explosion/sprite_14.png')
        ani_E15 = pygame.image.load('images/explosion/sprite_15.png')
        ani_E16 = pygame.image.load('images/explosion/sprite_16.png')
        ani_E17 = pygame.image.load('images/explosion/sprite_17.png')
        
        ani_E = pyganim.PygAnimation([(ani_E1, 1.1), (ani_E2, 1.1), (ani_E3, 1.1), (ani_E4, 1.1), (ani_E5, 1.1), \
            (ani_E6, 1.1), (ani_E7, 1.1), (ani_E8, 1.1), (ani_E9, 1.1), (ani_E10, 1.1),\
            (ani_E11, 1.1), (ani_E12, 1.1), (ani_E13, 1.1), (ani_E14, 1.1), (ani_E15, 1.1), \
            (ani_E16, 1.1), (ani_E17, 1.1)], False)
        #ani_conduct_explosion = pyganim.PygConductor([ani_E])
        self.ani_conduct.pause()
        ani_E.play()
        self.ani_conduct.play()
        ani_E.blit(self.x, self.y)
        
    def collide(self, object):
        if type(object) is Water:
            self.delete = True
        
