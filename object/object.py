import math, pygame

class Object(pygame.sprite.Sprite):

    def __init__(self, dimension):
        """ Constructor """
        self.x = 0
        self.old_x = 0
        self.y = 0
        self.old_y = 0
        
        self.dimension = dimension

        self.max_x = 800 - dimension
        self.min_x = 0
    	self.max_y = 600 - dimension
    	self.min_y = 0

    	self.red = 255
    	self.green = 0
    	self.blue = 0
    	self.width = 3

        self.image = None
        self.delete = False

    def draw(self, surface):
        if self.image is None:
            pygame.draw.rect(surface, (self.red, self.green, self.blue), (self.x, self.y, self.dimension, self.dimension), self.width)
        else:
            surface.blit(self.image, (self.x, self.y))

    def check_collision(self, object):
	## This has a bug, the boundaries overlap - causing it to always hit something
        #if (math.fabs(self.x - object.x) <= (self.dimension - 1) and math.fabs(self.y - object.y) <= (self.dimension - 1)): # reducing limit by 1 kinda fixed it
        #if object.x > self.x and object.x < (self.x + self.dimension) and object.y > self.y and object.y < (self.y + self.dimension):
        selfRect = pygame.Rect(self.x, self.y, self.dimension - 2, self.dimension - 2)
        objectRect = pygame.Rect(object.x, object.y, object.dimension - 2, object.dimension- 2)
        if selfRect.colliderect(objectRect):
            return True
        else:
            return False

    def collide(self, object):
        if type(object).__name__ == 'Water':
            print "[Info] Collided with Water" 
        elif type(object).__name__ == 'Dirt':
            print "[Info] Collided with Dirt"
        elif type(object).__name__ == 'Object':
            print "[Info] Collided with Object"
        else:
            print "[Error] Collided with unknown Object"
        self.x = self.old_x
        self.y = self.old_y

    def setPos(self, xPos, yPos):
	    self.old_x = xPos
	    self.old_y = yPos
	    self.x = xPos
	    self.y = yPos
        
    def speedBump(self, max_x_speed, max_y_speed):
        if self.x > self.old_x:
            self.x = self.old_x + max_x_speed
        if self.x < self.old_x:
            self.x = self.old_x - max_x_speed
        if self.y > self.old_y:
            self.y = self.old_y + max_y_speed
        if self.y < self.old_y:
            self.y = self.old_y - max_y_speed      
