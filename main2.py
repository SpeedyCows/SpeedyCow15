import pygame, os, sys

from object.object import *
from object.player_ant import *
from object.water import Water
from object.dirt import Dirt
from object.crazyant import CrazyAnt
from object.queen import Queen
from board import Board

SQUARE_SIZE = 40
FONT_SIZE = 20
FONT_COLOR = (255, 0, 0)

def HUD(screen, ant):
    font = pygame.font.Font(None, FONT_SIZE)
    screen.blit(font.render("Score: " + str(ant.score), True, FONT_COLOR), (0, 0))
    screen.blit(font.render("Lives: " + str(ant.lives), True, FONT_COLOR), (0, 1*FONT_SIZE))
    screen.blit(font.render("Power ups", True, FONT_COLOR), (0, 2*FONT_SIZE))
    screen.blit(font.render("   Sugar: " + str(ant.sugar), True, FONT_COLOR), (0, 3*FONT_SIZE))
    screen.blit(font.render("   Leaves: " + str(ant.leaves), True, FONT_COLOR), (0, 4*FONT_SIZE))

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
    object1 = Player_Ant(SQUARE_SIZE)
    objects.append(object1)
    object2 = Water(SQUARE_SIZE)
    object2.setPos(280, 280)
    objects.append(object2)
    crazyAnt = CrazyAnt(SQUARE_SIZE, object1)
    crazyAnt.setPos(500, 500)
    objects.append(crazyAnt)

    #Create the board
    board = Board(screen)
    staticObjects = board.asList()
    queen = Queen(SQUARE_SIZE)
    queen.setPos(420, 420)
    staticObjects.append(queen)

    started = False
    while True:
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
        object1.handle_keys()
            
        for dirt in staticObjects:
            if (object1.check_collision(dirt)):
                object1.collide(dirt)
                #staticObjects.remove(dirt)
                if (dirt.delete == True):
                    staticObjects.remove(dirt)


        for dirt in staticObjects:
            dirt.draw(screen)

        queen.doSomething()
                
        for object3 in objects:
            for object4 in objects:
                if (object3 != object4):
                    if (object3.check_collision(object4)):
                        object3.collide(object4)
                crazyAnt.searchForPlayer()
                crazyAnt.draw(screen)
            object3.draw(screen)

	HUD(screen, object1)

        pygame.display.update() # update the screen

        clock.tick(60)

main()
