import math
import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self):
        """ Constructor """

        self.x = 0
        self.old_x = 0
        self.y = 0
        self.old_y = 0

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

