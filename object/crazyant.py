from object import Object
import pygame, time
from random import Random

class CrazyAnt(Object):
    pause = 0
    def __init__(self,dimension, playerAnt):
        global pause
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

    def image_rotate(self, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

    def searchForPlayer(self):
        global pause
        if(self.timeForPause[pause] == self.counter):
            randDir = self.rand.randint(0, 3)
            self.image = pygame.transform.rotate(self.image, self.direction[randDir] - self._direction)
            self._direction = self.direction[randDir]
            pause = self.rand.randint(0, 12)
            self.counter = 0
        else:
            self.counter += 1

    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.image)
