from object import Object
import pygame

class Player_Ant(Object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        super(Player_Ant, self).__init__()

        self.image = pygame.image.load('images/ant.png')
        self.image = pygame.transform.scale(self.image, (40, 40))

    def image_rotate(self, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.image)

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

