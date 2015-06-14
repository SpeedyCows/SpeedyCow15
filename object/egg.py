from object import Object
import pygame, random, pyganim

class Egg(Object):

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Egg, self).__init__(dimension)

        # Queen Animation
        ani_E1 = pygame.image.load('images/egg/egg1.png')
        ani_E2 = pygame.image.load('images/egg/egg2.png')
        ani_E3 = pygame.image.load('images/egg/egg3.png')
        ani_E4 = pygame.image.load('images/egg/egg4.png')
        ani_E5 = pygame.image.load('images/egg/egg5.png')
        ani_E6 = pygame.image.load('images/egg/egg6.png')
        ani_E7 = pygame.image.load('images/egg/egg7.png')
        ani_E8 = pygame.image.load('images/egg/egg8.png')
        self.ani_E = pyganim.PygAnimation([(ani_E1, .1), (ani_E2, .1), (ani_E3, .1), (ani_E4, .1), (ani_E5, .1), (ani_E6, .1), (ani_E7, .1), (ani_E8, .1)])
        self.ani_E.scale((self.dimension, self.dimension))

        # start all animations
        self.ani_conduct = pyganim.PygConductor([self.ani_E])
        self.ani_conduct.play()

        # initial animation direction to draw
        self.ani = self.ani_E

    def collide(self, object):
       if type(object).__name__ == 'Player_Ant':
          object.lives += 1
          self.delete = True
       elif type(object).__name__ == 'Water':
          self.delete = True
       elif type(object).__name__ == 'Dirt':
          object.delete = True
       elif type(object).__name__ == 'Boulder':
          self.delete = True
       elif type(object).__name__ == 'CrazyAnt':
          self.delete = True
