from object import Object
import pygame, random, pyganim

class Queen(Object):

    def __init__(self, dimension):
        """ The constructor of the class """
        super(Queen, self).__init__(dimension)

        # Queen Animation
        ani_Q1 = pygame.image.load('images/queen/queenant1.png')
        ani_Q2 = pygame.image.load('images/queen/queenant2.png')
        ani_Q3 = pygame.image.load('images/queen/queenant3.png')
        ani_Q4 = pygame.image.load('images/queen/queenant4.png')
        ani_Q5 = pygame.image.load('images/queen/queenant5.png')
        ani_Q6 = pygame.image.load('images/queen/queenant6.png')
        ani_Q7 = pygame.image.load('images/queen/queenant7.png')
        ani_Q8 = pygame.image.load('images/queen/queenant8.png')
        self.ani_Q = pyganim.PygAnimation([(ani_Q1, .1), (ani_Q2, .1), (ani_Q3, .1), (ani_Q4, .1), (ani_Q5, .1), (ani_Q6, .1), (ani_Q7, .1), (ani_Q8, .1)])
        self.ani_Q.scale((self.dimension, self.dimension))

        # start all animations
        self.ani_conduct = pyganim.PygConductor([self.ani_Q])
        self.ani_conduct.play()

        # initial animation direction to draw
        self.ani = self.ani_Q

    def move(self):
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
        self.checkBoundaries()

    def dropEgg(self):
        return

    def doSomething(self):
        self.move()
        self.dropEgg()

    def collide(self, object):
       if type(object).__name__ == 'Player_Ant':
          object.score += object.sugar * 2
          object.score += object.leaves
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
