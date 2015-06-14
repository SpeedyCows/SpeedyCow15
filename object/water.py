from object import Object
import pygame
import random

class Water(Object):  # represents the water, not the game

    def __init__(self, dimension, board_width, board_height):
        """ The constructor of the class """
        super(Water, self).__init__(dimension)
        
        self.red = 0
        self.green = 0
        self.blue = 255
        self.width = 1

        self.image = pygame.image.load('images/water_resized.jpeg')
        self.image = pygame.transform.scale(self.image, (dimension, dimension))

        self.x_speed = 0
        self.y_speed = 0
        
        self.board_width = board_width
        self.board_height = board_height

	self.old_old_x = 0
	self.old_old_y = 0

        self.y_acceleration = .2

    def fall(self):
        self.old_old_x = self.old_x
        self.old_old_y = self.old_y
        self.old_x = self.x
        self.old_y = self.y

        self.x += self.x_speed
        self.y += self.y_speed

        self.y_speed += self.y_acceleration

    def collide(self, object):
        if (type(object) is Water):
            self.x_speed = -self.x_speed
        else:
            self.y_speed = 0
            if (self.x_speed == 0):
                if (random.randint(0, 1) == 0):
                    self.x_speed = -3
                else:
                    self.x_speed = 3
            elif (self.old_old_x == self.old_x and self.old_old_y == self.old_y):
                self.x_speed = 0

        self.x = self.old_x
        self.y = self.old_y

    def isMovable(self):
        return True
        
    def inBetweenLoops(self):
        self.fall()
        if self.x < 0:
            self.x = self.old_x
        elif self.x + self.dimension > self.board_width:
            self.x = self.old_x
        if self.y < 0:
            self.y = self.old_y
        elif self.y + self.dimension > self.board_height:
            self.y = self.old_y
