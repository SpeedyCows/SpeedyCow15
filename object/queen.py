from object import Object
import pygame
import random

class Queen(Object):

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Queen, self).__init__(dimension)

        self.image = pygame.image.load('images/crown.jpg')
        self.image = pygame.transform.scale(self.image, (dimension, dimension))

    def move(self):
	direction = random.randint(1,4)
        self.old_x = self.x
        self.old_y = self.y
        if direction == 1: # move right
            self.x + 1
        elif direction == 2: # move left
            self.x - 1
	elif direction == 3: # move down
            self.y + 1
        elif direction == 4: # move up
            self.y - 1

    def dropEgg(self):
        return

    def dropEnemy(self):
        return

    def doSomething(self):
        self.move()
        self.dropEgg()
        self.dropEnemy()

    def collide(self, object):
        if (type(object) is player_ant.Player_Ant):
            self.delete = True

    def isMovable(self):
        return True
