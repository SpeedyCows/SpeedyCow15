from object import Object
import pygame

class Water(Object):  # represents the water, not the game
    def __init__(self):
        """ The constructor of the class """
        super(Water, self).__init__()

        self.image = pygame.image.load('images/water.jpeg')
        self.image = pygame.transform.scale(self.image, (40, 40))

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))
