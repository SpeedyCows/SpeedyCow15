import pygame, os, sys, time

from object.object import *
from object.player_ant import *
from object.water import Water
from object.dirt import Dirt
from object.crazyant import CrazyAnt
from object.queen import Queen
from board import Board

SQUARE_SIZE = 40
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)

def HUD(screen, ant):
    font = pygame.font.Font(None, FONT_SIZE)
    screen.blit(font.render("Score: " + str(ant.score), True, FONT_COLOR), (0, 0))
    screen.blit(font.render("Lives: " + str(ant.lives), True, FONT_COLOR), (0, 1*FONT_SIZE))
    screen.blit(font.render("Power ups", True, FONT_COLOR), (0, 2*FONT_SIZE))
    screen.blit(font.render("   Sugar: " + str(ant.sugar), True, FONT_COLOR), (0, 3*FONT_SIZE))
    screen.blit(font.render("   Leaves: " + str(ant.leaves), True, FONT_COLOR), (0, 4*FONT_SIZE))
    if(ant.getRemianingLives() == 0):
        screen.blit(font.render("YOU LOOSE!!!!!! ", True, FONT_COLOR), (350, 300))

def processPYGame():
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit() # quit the screen
           sys.exit(1)

def main():
    pygame.init()
    background = pygame.image.load("images/grass.jpg")
    backgroundRect = background.get_rect()
    screen = pygame.display.set_mode((800, 600))

    clock = pygame.time.Clock()

    objects = []
    ant = Player_Ant(SQUARE_SIZE)
    objects.append(ant)
    object2 = Water(SQUARE_SIZE)
    object2.setPos(280, 280)
    objects.append(object2)
    crazyAnt = CrazyAnt(SQUARE_SIZE, ant, 'e')
    crazyAnt.setPos(500, 500)
    objects.append(crazyAnt)
    numberOfCrazyAnts = 1
    #Create the board
    board = Board(screen)
    staticObjects = board.asList()
    enemyAntList = []
    enemyAntList.append(crazyAnt)
    #print "[DEBUG] Setting up world"
    #dirts = []
    #DIRT_SIZE = SQUARE_SIZE / 2
    #for x in xrange(800 / DIRT_SIZE):
    #    for y in xrange(600 / DIRT_SIZE):
    #        if not (y == 0 and x == 0):
    #            dirt = Dirt(DIRT_SIZE)
    #            dirt.setPos(x * DIRT_SIZE, y * DIRT_SIZE)
    #            #objects.append(dirt)
    #print "[DEBUG] Done Setting up world"
    movableObjects, staticObjects = board.getObjects()
    movableObjects += [ant]
    movableObjects += [crazyAnt]

    queen = Queen(SQUARE_SIZE)
    queen.setPos(420, 420)
    staticObjects.append(queen)

    started = False
    while True:
        t = time.clock()
        print t
        if(t/20 > numberOfCrazyAnts):
            numberOfCrazyAnts += 1
            crazyAnt = CrazyAnt(SQUARE_SIZE, ant, 'e')
            movableObjects += crazyAnt

        screen.blit(background, backgroundRect)
        if not started:
           font = pygame.font.Font(None, 50)
           mes = font.render("Press <ENTER> to Start", True, (255, 0, 0))
           screen.blit(mes, (200, 400))
           pygame.display.update() # update the screen
           while True:
		 processPYGame()
                 key = pygame.key.get_pressed()
                 if key[pygame.K_RETURN]:
                    started = True
                    break

	processPYGame()

        ant.inBetweenLoops()
        for object in objects:
            object.inBetweenLoops()

        ant.handle_keys()

        for dirt in staticObjects:
            if (ant.check_collision(dirt)):
                ant.collide(dirt)
                #staticObjects.remove(dirt)
                if (dirt.delete == True):
                    staticObjects.remove(dirt)
            for crazyAnt in enemyAntList:
                if(crazyAnt.check_collision(dirt)):
                    crazyAnt.collide(dirt)

                    if(dirt.delete == True):
                        staticObjects.remove(dirt)

        for dirt in staticObjects:
            dirt.draw(screen)

        for object3 in objects:
            for object4 in objects:
                ant.handle_keys()

        queen.move()

        for staticObject in staticObjects:
            for movableObject in movableObjects:
                if (movableObject.check_collision(staticObject)):

                    #collide both ways
                    movableObject.collide(staticObject)
                    staticObject.collide(movableObject)

                    if (staticObject.delete == True):
                        staticObjects.remove(staticObject)

                    if(CrazyAnt.check_collision(crazyAnt, staticObject)):
                        crazyAnt.collide(staticObject)



        #draw all objects
        for obj in staticObjects + movableObjects:
            obj.draw(screen)

        #collide movable objects against each other
        for object3 in movableObjects:
            for object4 in movableObjects:
                if (object3 != object4):
                    if (object3.check_collision(object4)):
                        object3.collide(object4)
                for crazyAnt in enemyAntList:
                    crazyAnt.searchForPlayer()
            object3.draw(screen)

	HUD(screen, ant)

        pygame.display.update() # update the screen

        clock.tick(30)

main()
