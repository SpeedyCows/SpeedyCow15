from object import Object
from dirt import Dirt
import pygame
import random
 
class Leaf(Object):  # represents the water, not the game
    MAX_SPEED = 2

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Leaf, self).__init__(dimension)
        
        self.image = pygame.image.load('images/leaf.png')
        self.image = pygame.transform.scale(self.image, (self.dimension, self.dimension))        
        
        self.red = 0
        self.green = 255
        self.blue = 0
        self.width = 1
        
        self.xSpeed = Leaf.MAX_SPEED
        self.ySpeed = Leaf.MAX_SPEED
        
    def collide(self, object):

        self.old_x = self.x
        self.old_y = self.y
        if type(object).__name__ == 'Player_Ant':
            self.delete = True
            
        else:
            selfRect = pygame.Rect(self.x, self.y, self.dimension, self.dimension)
            otherRect = pygame.Rect(object.x, object.y, object.dimension, object.dimension)
            if selfRect.colliderect(otherRect):
                self.xSpeed = random.randint(-1 * Leaf.MAX_SPEED, Leaf.MAX_SPEED)
                self.ySpeed = random.randint(-1 * Leaf.MAX_SPEED, Leaf.MAX_SPEED)
        
    def inBetweenLoops(self):
        self.setPos(self.x + self.xSpeed, self.y + self.ySpeed)
        
    def isMovable(self):
        return True
