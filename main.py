import pygame
import os

# it is better to have an extra variable, than an extremely long line.
img_path = 'images/ant.png'


class Ant(pygame.sprite.Sprite):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load(img_path)

        # the bird's position
        self.x = 0
        self.y = 0

        # direction of the ant
        self._direction = 0
    def image_rotate(self, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.image)

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        angle = 90
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
            self.image = pygame.transform.rotate(self.image, 270 - self._direction)
            self._direction = 270
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
            self.image = pygame.transform.rotate(self.image, 90 - self._direction)
            self._direction = 90
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
            self.image = pygame.transform.rotate(self.image, 0 - self._direction)
            self._direction = 0
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
            self.image = pygame.transform.rotate(self.image, 180 - self._direction)
            self._direction = 180

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))


pygame.init()
background = pygame.image.load("images/grass.jpg")
backgroundRect = background.get_rect()
screen = pygame.display.set_mode((800, 600))

ant = Ant() # create an instance
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    ant.handle_keys() # handle the keys

    #screen.fill((255,255,255)) # fill the screen with white
    screen.blit(background, backgroundRect)
    ant.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    clock.tick(100)