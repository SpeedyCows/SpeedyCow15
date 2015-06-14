from object import Object
from water import Water
from sugar import Sugar
from block import Boulder
from dirt import Dirt
from leaf import Leaf
from fire import Fire
import pygame, sys, pyganim

FONT_SIZE = 20
FONT_COLOR = (255, 0, 0)

class Player_Ant(Object):  # represents the bird, not the game
    def __init__(self, dimension):
        """ The constructor of the class """
        super(Player_Ant, self).__init__(dimension)

        # Right Animation
        ani_R1 = pygame.image.load('images/ant/sprite_b_ant_right1.png')
        ani_R2 = pygame.image.load('images/ant/sprite_b_ant_right2.png')
        ani_R3 = pygame.image.load('images/ant/sprite_b_ant_right3.png')
        ani_R4 = pygame.image.load('images/ant/sprite_b_ant_right4.png')
        self.ani_R = pyganim.PygAnimation([(ani_R1, .1), (ani_R2, .1), (ani_R3, .1), (ani_R4, .1)])
        self.ani_R.scale((self.dimension, self.dimension))

        # Left Animation
        ani_L1 = pygame.image.load('images/ant/sprite_b_ant_left1.png')
        ani_L2 = pygame.image.load('images/ant/sprite_b_ant_left2.png')
        ani_L3 = pygame.image.load('images/ant/sprite_b_ant_left3.png')
        ani_L4 = pygame.image.load('images/ant/sprite_b_ant_left4.png')
        self.ani_L = pyganim.PygAnimation([(ani_L1, .1), (ani_L2, .1), (ani_L3, .1), (ani_L4, .1)])
        self.ani_L.scale((self.dimension, self.dimension))

        # Down Animation
        ani_D1 = pygame.image.load('images/ant/sprite_b_ant_down1.png')
        ani_D2 = pygame.image.load('images/ant/sprite_b_ant_down2.png')
        ani_D3 = pygame.image.load('images/ant/sprite_b_ant_down3.png')
        ani_D4 = pygame.image.load('images/ant/sprite_b_ant_down4.png')
        self.ani_D = pyganim.PygAnimation([(ani_D1, .1), (ani_D2, .1), (ani_D3, .1), (ani_D4, .1)])
        self.ani_D.scale((self.dimension, self.dimension))

        # Up Animation
        ani_U1 = pygame.image.load('images/ant/sprite_b_ant_up1.png')
        ani_U2 = pygame.image.load('images/ant/sprite_b_ant_up2.png')
        ani_U3 = pygame.image.load('images/ant/sprite_b_ant_up3.png')
        ani_U4 = pygame.image.load('images/ant/sprite_b_ant_up4.png')
        self.ani_U = pyganim.PygAnimation([(ani_U1, .1), (ani_U2, .1), (ani_U3, .1), (ani_U4, .1)])
        self.ani_U.scale((self.dimension, self.dimension))

        # start all animations
        self.ani_conduct = pyganim.PygConductor([self.ani_R, self.ani_L, self.ani_D, self.ani_U])
        self.ani_conduct.play()

        # initial animation direction to draw
        self.ani = self.ani_D

        self.move = (0, 0)

        self.powerup = None


        self.initial_score = 0
        self.score = self.initial_score
        self.initial_lives = 3
        self.lives = self.initial_lives
        self.initial_leaves = 0
        self.leaves = self.initial_leaves
        self.initial_sugar = 0
        self.sugar = self.initial_sugar

        self.initial_speed = 5
        self.speed = self.initial_speed
    	self._direction = 0


    def handle_mouse(self, event):"""
        delta_x = self.x - event.pos[0]
        delta_y = self.y - event.pos[1]

        if delta_x > 0:
            self.move_left()
        elif delta_x < 0:
            self.move_right()
        if delta_y > 0:
            self.move_up()
        elif delta_y < 0:
            self.move_down()"""

    def handle_key(self, event):
        self.ani_conduct.play()

        if event.key == pygame.K_DOWN: # down key
            self.move_down()
        elif event.key == pygame.K_UP: # up key
            self.move_up()
        if event.key == pygame.K_RIGHT: # right key
            self.move_right()
        elif event.key == pygame.K_LEFT: # left key
            self.move_left()
        elif event.key == pygame.K_SPACE:
            if (self.powerup == None):
                print "You have no powerup"
            if (self.powerup == "Sugar"):
                print "Using sugar"
                self.powerup = None
                self.speed = 2 * self.speed
                self.sugar -= 1
                if self.sugar < 0:
                   self.sugar = 0
        elif event.key == pygame.K_ESCAPE:
                sys.exit(0)
    def move_up(self):
        self.move = (0, 0 - self.speed)
        self.ani = self.ani_U
        self._direction = 90

    def move_down(self):
        self.move = (0, self.speed)
        self.ani = self.ani_D
        self._direction = 270

    def move_right(self):
        self.move = (self.speed, 0)
        self.ani = self.ani_R
        self._direction = 0

    def move_left(self):
        self.move = (0 - self.speed, 0)
        self.ani = self.ani_L
        self._direction = 180

    def update_pos(self):
        self.old_x = self.x
        self.old_y = self.y
        new_pos = self.x + self.move[0], self.y + self.move[1]
        if new_pos[0] <= self.max_x and new_pos[0] >= self.min_x:
            self.x = new_pos[0]
        if new_pos[1] <= self.max_y and new_pos[1] >= self.min_y:
            self.y = new_pos[1]

    def pause_ani(self):
        self.ani_conduct.pause()
        self.move = (0, 0)

    def collide(self, object):
        if type(object) is Dirt:
            self.x = self.old_x
            self.y = self.old_y
            object.life -= 1
            if object.life == 0:
                object.delete = True
        elif type(object).__name__ == 'Dirt' and object.empty:
            return
        elif type(object) is Water:
            self.minusLife()
            return
        elif type(object) is Fire:
            self.minusLife()
            object.explode()
            return
        elif type(object) is Sugar:
            print "PICKED UP SUGAR"  
            self.powerup = "Sugar"
            self.sugar += 1
        elif type(object) is Leaf:
            print "PICKED UP Leaf"  
            self.powerup = "Leaf"
            self.leaves += 1
        # Slow the ant down to the max travelling speed of the block
        elif type(object) is Boulder:
            self.speedBump(object.xSpeed, object.ySpeed)
        else:
            pass

    def image_rotate(self, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

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
