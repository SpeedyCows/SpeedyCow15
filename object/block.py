from object import Object
from dirt import Dirt
import pygame

class Block(Object):  # represents the water, not the game
    MAX_SPEED = 2

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Block, self).__init__(dimension)
        
        self.red = 0
        self.green = 0
        self.blue = 255
        self.width = 1
        
        self.direction = 0
        self.xSpeed = Block.MAX_SPEED
        self.ySpeed = Block.MAX_SPEED
        
    def collide(self, object):

        self.old_x = self.x
        self.old_y = self.y
        if type(object).__name__ == 'Player_Ant':
            self.direction = object._direction
            if object._direction == 0:
                self.x += self.xSpeed         
            elif object._direction == 90:
                self.y -= self.ySpeed
                self.ySpeed = Block.MAX_SPEED
            elif object._direction == 180:
                self.x -= self.xSpeed
            elif object._direction == 270:
                self.y += self.ySpeed
            
        elif type(object) is Dirt:
            if self.direction == 0 and object.x < self.x + self.dimension:
                self.x = object.x - self.dimension
                self.xSpeed = 0
            elif self.direction == 90 and object.y + object.dimension > self.y:
                self.y = object.y + object.dimension
                self.ySpeed = 0
            elif self.direction == 180 and object.x + object.dimension > self.x:
                self.x = object.x + object.dimension
                self.xSpeed = 0
            elif self.direction == 270 and object.y < self.y + self.dimension:
                self.y = object.y - self.dimension
                self.ySpeed
        return      
        
    def inBetweenLoops(self):
        self.xSpeed = Block.MAX_SPEED
        self.ySpeed = Block.MAX_SPEED