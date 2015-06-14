import pygame, os

from object.object import *
from object.player_ant import *
from object.water import Water
from object.dirt import Dirt
from object.crazyant import CrazyAnt

from object.pyganim import *
PLAYER_SIZE = 80
SQUARE_SIZE = 40

def main():
    pygame.init()
    background = pygame.image.load("images/grass.jpg")
    backgroundRect = background.get_rect()
    screen = pygame.display.set_mode((800, 600))

    #ant = Ant() # create an instance
    clock = pygame.time.Clock()

    objects = []
    object1 = Player_Ant(PLAYER_SIZE)
    objects.append(object1)
    object2 = Water(SQUARE_SIZE)
    object2.setPos(280, 280)
    objects.append(object2)
    crazyAnt = CrazyAnt(SQUARE_SIZE, object1)
    crazyAnt.setPos(500, 500)
    objects.append(crazyAnt)

    print "[DEBUG] Setting up world"
    dirts = []
    DIRT_SIZE = SQUARE_SIZE / 2
    for x in xrange(800 / DIRT_SIZE):
        for y in xrange(600 / DIRT_SIZE):
            if not (y == 0 and x == 0):
                dirt = Dirt(DIRT_SIZE)
                dirt.setPos(x * DIRT_SIZE, y * DIRT_SIZE)
                #objects.append(dirt)
    print "[DEBUG] Done Setting up world"

    keycount = 0
    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the screen
                running = False
            elif event.type == pygame.KEYDOWN:
                #need to count key down so that we can track when they are released
                keycount += 1
                object1.handle_key(event)
            elif event.type == pygame.KEYUP:
                #only pause if num of key down is now 0
                keycount -= 1
                if keycount <= 0:
                    object1.pause_ani()

        #ant.handle_keys() # handle the keys

        #Update ant position
        object1.update_pos()

        #screen.fill((255,255,255)) # fill the screen with black
        screen.blit(background, backgroundRect)

            
        for dirt in dirts:
            if (object1.check_collision(dirt)):
                dirts.remove(dirt)

        for dirt in dirts:
            dirt.draw(screen)
                
        for object3 in objects:
            for object4 in objects:
                if (object3 != object4):
                    if (object3.check_collision(object4)):
                        object3.collide(object4)
                crazyAnt.searchForPlayer()
                crazyAnt.draw(screen)
            object3.draw(screen)

	font = pygame.font.Font(None, 50)
	mes = font.render("Press <SPACE> to Start", True, (255, 0, 0))
	screen.blit(mes, (100, 100))

        #ant.draw(screen) # draw the bird to the screen
        #pygame.draw.rect(screen, (255, 0, 0), (20, 20, 40, 40), 2)
        pygame.display.update() # update the screen

        clock.tick(100)

main()
