from object import Object
import pygame

class Player_Ant(Object):  # represents the bird, not the game
    def __init__(self, dimension):
        """ The constructor of the class """
        super(Player_Ant, self).__init__(dimension)

        self.image = pygame.image.load('images/ant.png')
        self.image = pygame.transform.scale(self.image, (self.dimension, self.dimension))

	self._direction = 0
        
    def handle_keys(self):
        """ Handles Keys """

        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            if (self.y + dist) <= self.max_y: 
                self.old_y = self.y
                self.y += dist # move dow
            self.image = pygame.transform.rotate(self.image, 270 - self._direction)
            self._direction = 270
        elif key[pygame.K_UP]: # up key
            if (self.y - dist) >= self.min_y: 
                self.old_y = self.y
                self.y -= dist # move up
            self.image = pygame.transform.rotate(self.image, 90 - self._direction)
            self._direction = 90
        if key[pygame.K_RIGHT]: # right key
            if (self.x + dist) <= self.max_x: 
                self.old_x = self.x
                self.x += dist # move right
            self.image = pygame.transform.rotate(self.image, 0 - self._direction)
            self._direction = 0
        elif key[pygame.K_LEFT]: # left key
            if (self.x - dist) >= self.min_x: 
                self.old_x = self.x
                self.x -= dist # move left
            self.image = pygame.transform.rotate(self.image, 180 - self._direction)
            self._direction = 180

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

