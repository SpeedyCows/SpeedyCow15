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
	# this does not work to good!
        direction = random.choice((0, 1, 2, 3))
        self.old_x = self.x
        self.old_y = self.y
        if direction == 0: # move right
            self.x += 3
        elif direction == 1: # move left
            self.x -= 3
	elif direction == 2: # move down
            self.y += 3
        elif direction == 3: # move up
            self.y -= 3

    def dropEgg(self):
        return

    def doSomething(self):
        self.move()
        self.dropEgg()

    def collide(self, object):
       if type(object).__name__ == 'Player_Ant':
          object.score += object.sugar * 2
          object.score += object.leave
          object.leaves = 0
          object.sugar = 0
       elif type(object).__name__ == 'Water':
          object.x = object.old_x
          object.y = object.old_y
       elif type(object).__name__ == 'Dirt':
          object.x = object.old_x
          object.y = object.old_y
          object.life -= 1
          if object.life == 0:
             object.delete = True
       elif type(object).__name__ == 'Boulder':
            self.speedBump(object.xSpeed, object.ySpeed)

    def isMovable(self):
        return True
