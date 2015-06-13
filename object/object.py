import math, pygame

class Object(pygame.sprite.Sprite):
    def __init__(self):
        """ Constructor """

        self.max_x = 800 - 40
        self.min_x = 0
	self.max_y = 600 - 40
	self.min_y = 0

        self.x = 0
        self.old_x = 0
        self.y = 0
        self.old_y = 0

    def handle_keys(self):
        """ Handles Keys """

        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            if (self.y + dist) <= self.max_y: 
                self.old_y = self.y
                self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            if (self.y - dist) >= self.min_y: 
                self.old_y = self.y
                self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            if (self.x + dist) <= self.max_x: 
                self.old_x = self.x
                self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            if (self.x - dist) >= self.min_x: 
                self.old_x = self.x
                self.x -= dist # move left
            

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 40, 40), 3)
        #surface.blit(self.image, (self.x, self.y))

    def check_collision(self, object):
        if (math.fabs(self.x - object.x) <= 40 and math.fabs(self.y - object.y) <= 40):
            return True
        else:
            return False

    def collide(self, object):
        self.x = self.old_x
        self.y = self.old_y


    def setPos(self, xPos, yPos):
	self.old_x = xPos
	self.old_y = yPos
	self.x = xPos
	self.y = yPos
