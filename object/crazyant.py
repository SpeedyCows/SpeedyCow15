from object import Object
import pygame, pyganim
from random import Random
from dirt import Dirt
from block import Boulder

from water import Water
from queen import Queen
from fire import Fire

class CrazyAnt(Object):
    def __init__(self, dimension, playerAnt, difficulty):
        global pause
        global cPause
        global justRotated
        super(CrazyAnt, self).__init__(dimension)
        self.playerAnt = playerAnt
        self.image = pygame.image.load('images/ant.png')
        self.image = pygame.transform.scale(self.image, (self.dimension, self.dimension))

         # Right Animation
        ani_R1 = pygame.image.load('images/rant/sprite_r_ant_right1.png')
        ani_R2 = pygame.image.load('images/rant/sprite_r_ant_right2.png')
        ani_R3 = pygame.image.load('images/rant/sprite_r_ant_right3.png')
        ani_R4 = pygame.image.load('images/rant/sprite_r_ant_right4.png')
        self.ani_R = pyganim.PygAnimation([(ani_R1, .1), (ani_R2, .1), (ani_R3, .1), (ani_R4, .1)])
        self.ani_R.scale((self.dimension, self.dimension))

        # Left Animation
        ani_L1 = pygame.image.load('images/rant/sprite_r_ant_left1.png')
        ani_L2 = pygame.image.load('images/rant/sprite_r_ant_left2.png')
        ani_L3 = pygame.image.load('images/rant/sprite_r_ant_left3.png')
        ani_L4 = pygame.image.load('images/rant/sprite_r_ant_left4.png')
        self.ani_L = pyganim.PygAnimation([(ani_L1, .1), (ani_L2, .1), (ani_L3, .1), (ani_L4, .1)])
        self.ani_L.scale((self.dimension, self.dimension))

        # Down Animation
        ani_D1 = pygame.image.load('images/rant/sprite_r_ant_down1.png')
        ani_D2 = pygame.image.load('images/rant/sprite_r_ant_down2.png')
        ani_D3 = pygame.image.load('images/rant/sprite_r_ant_down3.png')
        ani_D4 = pygame.image.load('images/rant/sprite_r_ant_down4.png')
        self.ani_D = pyganim.PygAnimation([(ani_D1, .1), (ani_D2, .1), (ani_D3, .1), (ani_D4, .1)])
        self.ani_D.scale((self.dimension, self.dimension))

        # Up Animation
        ani_U1 = pygame.image.load('images/rant/sprite_r_ant_up1.png')
        ani_U2 = pygame.image.load('images/rant/sprite_r_ant_up2.png')
        ani_U3 = pygame.image.load('images/rant/sprite_r_ant_up3.png')
        ani_U4 = pygame.image.load('images/rant/sprite_r_ant_up4.png')
        self.ani_U = pyganim.PygAnimation([(ani_U1, .1), (ani_U2, .1), (ani_U3, .1), (ani_U4, .1)])
        self.ani_U.scale((self.dimension, self.dimension))

        # start all animations
        self.ani_conduct = pyganim.PygConductor([self.ani_R, self.ani_L, self.ani_D, self.ani_U])
        self.ani_conduct.play()

        # initial animation direction to draw
        self.ani = self.ani_R


        self._direction = 0
        self.rand = Random()
        self.rotationTracekr = 0
        self.counterVars = [0, 10001, 12001, 13001, 14001, 15001, 16001, 17001, 18001, 19001, 10001, 11001, 12001, 13001]
        self.timeForPause = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
        self.direction = [0, 90, 180, 270]
        self.ani_direction = [self.ani_R, self.ani_U, self.ani_L, self.ani_D]
        justRotated = 0
        pause = self.rand.randint(0, 13)
        cPause = self.rand.randint(0, 13)
        self.counter = 0
        if(difficulty == 'h'):
            self.speed = 0.09
        elif(difficulty == 'm'):
            self.speed = 0.07
        else:
            self.speed = 0.05

    def image_rotate(self, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

    def aggresiveSearchForPlayer(self):
        global pause
        global cPause
        if(self.timeForPause[pause] >= self.counter):
            randDir = self.rand.randint(0, 3)
            self.image = pygame.transform.rotate(self.image, self.direction[randDir] - self._direction)
            self._direction = self.direction[randDir]
            self.ani = self.ani_direction[randDir]
            pause = self.rand.randint(0, 12)
            self.counter = 0
            self.checkDirection()
        else:
            self.counter += 1
            self.checkDirection()

    # Kind of the init function for ants
    def searchForPlayer(self):
        global pause
        global cPause
        global justRotated
        if(self.timeForPause[pause] >= self.counterVars[cPause]):
            randDir = self.rand.randint(0, 3)
            if(justRotated >= 300):
                self.image = pygame.transform.rotate(self.image, self.direction[randDir] - self._direction)
                self._direction = self.direction[randDir]
                self.ani = self.ani_direction[randDir]
                justRotated = 0
            else:
                justRotated += 1
            pause = self.rand.randint(0, 13)
            cPause = self.rand.randint(0, 13)
            self.counter = 0
            self.checkDirection()
        else:
            pause = self.rand.randint(0, 13)
            cPause = self.rand.randint(0, 13)
            self.checkDirection()

    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.image)

    def checkDirection(self):
        global functionCounter
        #translate where to check for on the board.
        if(self._direction == 0):#Ant looks 5 to the right
            if(self.playerAnt.getXPosition() >= self.x and 
               self.playerAnt.getXPosition() <= self.x + 200 and
               self.x < self.max_x): #Then we move right
                self.old_x = self.x
                self.x += self.speed
        elif(self._direction == 90):#We look up
            if(self.playerAnt.getYPosition() <= self.y and 
               self.playerAnt.getYPosition() >= self.y - 200 and
               self.y > self.min_y): #Move u
                self.old_y = self.y
                self.y -= self.speed
        elif(self._direction == 180):#look left
            if(self.playerAnt.getXPosition() <= self.x and 
               self.playerAnt.getXPosition() >= self.x - 200 and
               self.x > self.min_x):#mvoe left
                self.old_x = self.x
                self.x -= self.speed
        elif(self._direction == 270):
            if(self.playerAnt.getYPosition() >= self.y and 
               self.playerAnt.getYPosition() <= self.y + 200 and 
               self.y < self.max_y):
                self.old_y = self.y
                self.y += self.speed

    def collide(self, obj):
        if type(obj) is Dirt:
            self.x = self.old_x
            self.y = self.old_y
            obj.life -= 1
            if obj.life == 0:
                obj.delete = True
        elif type(obj).__name__ == 'Dirt' and obj.empty:
            return
        elif type(obj) is Boulder:
            self.speedBump(obj.xSpeed, obj.ySpeed)
        # Slow the ant down to the max travelling speed of the block
        elif type(object) is Boulder or type(object) is Water or type(object) is Queen or type(object) is Fire:
            self.delete = True

        elif type(obj).__name__ == 'Player_Ant':
            self.playerAnt.minusLife()
            self.playerAnt

    def isMovable(self):
        return True
