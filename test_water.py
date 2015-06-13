import pygame, os

from object.object import *
from object.player_ant import *
from object.water import Water
from object.dirt import Dirt

SQUARE_SIZE = 40

def main():
    pygame.init()
    background = pygame.image.load("images/grass.jpg")
    backgroundRect = background.get_rect()
    screen = pygame.display.set_mode((800, 600))

    clock = pygame.time.Clock()

    objects = []
    objects2 = []
    object1 = Player_Ant(SQUARE_SIZE)
    objects.append(object1)

    # Setup squares here
    j = 0
    while j < 5:
        if (j == 2):
            j += 1
            continue
        square = Object(SQUARE_SIZE)
        square.setPos(280 + j*SQUARE_SIZE, 280)
        objects.append(square)
        objects2.append(square)
        j += 1

    # Setup water here
    i = 0
    waters = []
    while i < 5:
        water = Water(SQUARE_SIZE)
        water.setPos(280 + i*SQUARE_SIZE, 80)
        objects.append(water)
        objects2.append(water)
        waters.append(water)
        i += 1

    objects2.append(object1)

    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the screen
                running = False

        screen.fill((255,255,255)) # fill the screen with black

        object1.handle_keys()

        for object3 in objects:
            for object4 in objects:
                if (object3 != object4):
                    if (object3.check_collision(object4)):
                        object3.collide(object4)

        waters_remove = []
        for water in waters:
            water.fall()
            if water.y > 800:
                waters_remove.append(water)

        for water in waters_remove:
            waters.remove(water)
            objects.remove(water)
            objects2.remove(water)

        for object5 in objects2:
            object5.draw(screen)

        pygame.display.update() # update the screen

        clock.tick(100)

main()
