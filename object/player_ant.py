from object import Object
from water import Water
from sugar import Sugar
from block import Boulder
from dirt import Dirt
import pygame, sys

FONT_SIZE = 20
FONT_COLOR = (255, 0, 0)

class Player_Ant(Object):  # represents the bird, not the game
    def __init__(self, dimension):
        """ The constructor of the class """
        super(Player_Ant, self).__init__(dimension)

        self.image = pygame.image.load('images/ant.png')
        self.image = pygame.transform.scale(self.image, (self.dimension, self.dimension))

        self.powerup = None

        self.score = 0
        self.lives = 3
        self.leaves = 0
        self.sugar = 0

        self.initial_speed = 5
        self.speed = self.initial_speed
    	self._direction = 0
        
    def handle_keys(self):
        """ Handles Keys """

        key = pygame.key.get_pressed()
        #self.dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key 
            if (self.y + self.speed) <= self.max_y: 
                self.old_y = self.y
                self.y += self.speed # move down
            self.image = pygame.transform.rotate(self.image, 270 - self._direction)
            self._direction = 270
        if key[pygame.K_UP]: # up key
            if (self.y - self.speed) >= self.min_y: 
                self.old_y = self.y
                self.y -= self.speed # move up
            self.image = pygame.transform.rotate(self.image, 90 - self._direction)
            self._direction = 90
        if key[pygame.K_RIGHT]: # right key
            if (self.x + self.speed) <= self.max_x: 
                self.old_x = self.x
                self.x += self.speed # move right
            self.image = pygame.transform.rotate(self.image, 0 - self._direction)
            self._direction = 0
        if key[pygame.K_LEFT]: # left key
            if (self.x - self.speed) >= self.min_x:  
                self.old_x = self.x
                self.x -= self.speed # move left
            self.image = pygame.transform.rotate(self.image, 180 - self._direction)
            self._direction = 180
        if key[pygame.K_SPACE]:
            if (self.powerup == None):
                print "You have no powerup"
            if (self.powerup == "Sugar"):
                print "Using sugar"
                self.powerup = None
                self.speed = 2 * self.speed
                self.sugar -= 1
                if self.sugar < 0:
                   self.sugar = 0
        if key[pygame.K_ESCAPE]:
                sys.exit(0)

    def collide(self, object):
        if type(object) is Dirt:
            self.x = self.old_x
            self.y = self.old_y
            object.life -= 1
            if object.life == 0:
                object.delete = True
        elif type(object).__name__ == 'Dirt' and object.empty:
            return
        elif type(object).__name__ == 'Water':
            self.x = self.old_x
            self.y = self.old_y
            return
        elif type(object) is Sugar:
            print "PICKED UP SUGAR"  
            self.powerup = "Sugar"
            self.sugar += 1
            self.delete = True
        # Slow the ant down to the max travelling speed of the block
        elif type(object) is Boulder:
            self.speedBump(object.xSpeed, object.ySpeed)
        else:
            print "[Info] Collided with Dirt or something"

    def image_rotate(self, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.image)

    def getXPosition(self):
        return self.x

    def getYPosition(self):
        return self.y

    def minusLife(self):
        self.lives -= 1
        self.setPos(0, 0)
        self.speed = self.initial_speed
        
    def getRemianingLives(self):
        return self.lives

    def isMovable(self):
        return True
