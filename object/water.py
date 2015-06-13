from object import Object
import pygame

class Water(Object):  # represents the water, not the game
    WATER_DOWN = 0
    WATER_RIGHT = 1
    WATER_LEFT = 2

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Water, self).__init__(dimension)
        print "WATER!!!"
        
        self.red = 0
        self.green = 0
        self.blue = 255
        self.width = 1

        #self.image = pygame.image.load('images/water.jpeg')
        self.image = pygame.image.load('images/water_resized.jpeg')
        self.image = pygame.transform.scale(self.image, (dimension, dimension))
        
        self.direction = Water.WATER_DOWN
        self.speed = 1
        
    def move(self, object):
        if self.direction == Water.WATER_DOWN:
            self.y += speed
            
    def collide(self, object):

        return      