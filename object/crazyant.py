from object import Object
import pygame
from random import Random
from dirt import Dirt
from block import Block

class CrazyAnt(Object):
    def __init__(self, dimension, playerAnt, difficulty):
        global pause
        global timesMoved
        super(CrazyAnt, self).__init__(dimension)
        self.playerAnt = playerAnt
        self.image = pygame.image.load('images/ant.png')
        self.image = pygame.transform.scale(self.image, (self.dimension, self.dimension))
        self._direction = 0
        self.rand = Random()
        self.rotationTracekr = 0
        self.timeForPause = [200, 500, 700, 90, 10, 150, 300, 300, 400, 50, 10, 118, 120]
        self.direction = [0, 90, 180, 270]
        pause = self.rand.randint(0, 12)
        self.counter = 0
        timesMoved = 0
        if(difficulty == 'h'):
            self.speed = 4
        elif(difficulty == 'm'):
            self.speed = 3
        else:
            self.speed = 1

    def image_rotate(self, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

    # Kind of the init function for ants
    def searchForPlayer(self):
        global pause
        global found
        global timesMoved
        if(self.timeForPause[pause] == self.counter):
            randDir = self.rand.randint(0, 3)
            self.image = pygame.transform.rotate(self.image, self.direction[randDir] - self._direction)
            self._direction = self.direction[randDir]
            pause = self.rand.randint(0, 12)
            self.counter = 0
            timesMoved = 0
            self.checkDirection()
        else:
            self.counter += 1
            self.checkDirection()
    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.image)

    def checkDirection(self):
        #translate where to check for on the board.
        if(self._direction == 0):#Ant looks 5 to the right
            if(self.playerAnt.getXPosition() >= self.x and 
               self.playerAnt.getXPosition() <= self.x + 100 and
               self.x < self.max_x): #Then we move right
                self.old_x = self.x
                self.x += self.speed
        elif(self._direction == 90):#We look up
            if(self.playerAnt.getYPosition() <= self.y and 
               self.playerAnt.getYPosition() >= self.y - 100 and
               self.y > self.min_y): #Move u
                self.old_y = self.y
                self.y -= self.speed
        elif(self._direction == 180):#look left
            if(self.playerAnt.getXPosition() <= self.x and 
               self.playerAnt.getXPosition() >= self.x - 100 and
               self.x > self.min_x):#mvoe left
                self.old_x = self.x
                self.x -= self.speed
        elif(self._direction == 270):
            if(self.playerAnt.getYPosition() >= self.y and 
               self.playerAnt.getYPosition() <= self.y + 100 and 
               self.y < self.max_y):
                self.old_y = self.y
                self.y += self.speed

    def collide(self, object):
        if type(object) is Dirt:
            self.x = self.old_x
            self.y = self.old_y
            object.life -= 1
            if object.life == 0:
                object.delete = True
        elif type(object).__name__ == 'Dirt' and object.empty:
            return
        # Slow the ant down to the max travelling speed of the block
        elif type(object) is Block:
            self.speedBump(object.xSpeed, object.ySpeed)

        elif type(object).__name__ == 'Player_Ant':
            self.playerAnt.minusLife()
            self.playerAnt