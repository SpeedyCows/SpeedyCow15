import pygame, os

from object.object import *
from object.player_ant import *
from object.water import Water
from object.dirt import Dirt
from object.crazyant import CrazyAnt

SQUARE_SIZE = 40

def main():
    pygame.init()
    background = pygame.image.load("images/grass.jpg")
    backgroundRect = background.get_rect()
    screen = pygame.display.set_mode((800, 600))

    #ant = Ant() # create an instance
    clock = pygame.time.Clock()

    objects = []
    object1 = Player_Ant(SQUARE_SIZE)
    objects.append(object1)
    object2 = Object(SQUARE_SIZE)
    object2.setPos(280, 280)
    objects.append(object2)
    crazyAnt = CrazyAnt(SQUARE_SIZE, object1)
    crazyAnt.setPos(500, 500)
    objects.append(crazyAnt)
    
    
    #flag = 0
    #for x in xrange(800):
	#for y in xrange(600):
		#if (x % 100) == 80 and (y % 100) == 40:
		#	water = Water(SQUARE_SIZE)
		#	water.setPos(x, y)
		#	objects.append(water)
                 #       flag = ~flag
                  #      if flag == 0:
		#		dirt = Dirt(SQUARE_SIZE)
		#		dirt.setPos(x, y + SQUARE_SIZE)
		#		objects.append(dirt)

    print "[DEBUG] Setting up world"
    for x in xrange(800 / SQUARE_SIZE):
        for y in xrange(600 / SQUARE_SIZE):
            if not (y == 0 and x == 0) and not (x == 7 and y == 7):
                dirt = Dirt(SQUARE_SIZE)
                dirt.setPos(x * SQUARE_SIZE, y * SQUARE_SIZE)
              #  objects.append(dirt)
    print "[DEBUG] Done Setting up world"

    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the screen
                running = False

        #ant.handle_keys() # handle the keys

        screen.fill((255,255,255)) # fill the screen with black
        #screen.blit(background, backgroundRect)

        object1.handle_keys()

        for object3 in objects:
            for object4 in objects:
                if (object3 != object4):
                    if (object3.check_collision(object4)):
                        object3.collide(object4)
                crazyAnt.searchForPlayer()
                crazyAnt.draw(screen)
            object3.draw(screen)

        #ant.draw(screen) # draw the bird to the screen
        #pygame.draw.rect(screen, (255, 0, 0), (20, 20, 40, 40), 2)
        pygame.display.update() # update the screen

        clock.tick(100)

main()
