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
FONT_COLOR = (255, 255, 255)

def HUD(screen, ant):
    font = pygame.font.Font(None, FONT_SIZE)
    screen.blit(font.render("Score: " + str(ant.score), True, FONT_COLOR), (0, 0))
    screen.blit(font.render("Lives: " + str(ant.lives), True, FONT_COLOR), (0, 1*FONT_SIZE))
    screen.blit(font.render("Power ups", True, FONT_COLOR), (0, 2*FONT_SIZE))
    screen.blit(font.render("   Sugar: " + str(ant.sugar), True, FONT_COLOR), (0, 3*FONT_SIZE))
    screen.blit(font.render("   Leaves: " + str(ant.leaves), True, FONT_COLOR), (0, 4*FONT_SIZE))
    if(ant.getRemianingLives() == 0):
        screen.blit(font.render("YOU LOOSE!!!!!! ", True, FONT_COLOR), (250, 300))

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

    ant = Player_Ant(SQUARE_SIZE)
    crazyAnt = CrazyAnt(SQUARE_SIZE, ant, 'e')
    crazyAnt.setPos(500, 500)

    #Create the board
    board = Board(screen)
    movableObjects, staticObjects = board.getObjects()
    movableObjects += [ant]
    movableObjects += [crazyAnt]

    queen = Queen(SQUARE_SIZE)
    queen.setPos(420, 420)
    movableObjects.append(queen)

    started = False
    while True:
        screen.blit(background, backgroundRect)
        if not started:
           font = pygame.font.Font(None, 50)
           mes = font.render("Press <ENTER> to Start", True, (255, 0, 0))
           screen.blit(mes, (200, 250))
           pygame.display.update() # update the screen
           while True:
		 processPYGame()
                 key = pygame.key.get_pressed()
                 if key[pygame.K_RETURN]:
                    started = True
                    break
                 if key[pygame.K_ESCAPE]:
                    sys.exit(0)

	processPYGame()

        ant.inBetweenLoops()
        for object in movableObjects:
            object.inBetweenLoops()
            
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
                crazyAnt.searchForPlayer()

        for object3 in movableObjects:
            if (object3.delete == True):
                movableObjects.remove(object3)     
                
        for object3 in movableObjects:
            object3.draw(screen)

	HUD(screen, ant)

        pygame.display.update() # update the screen

        clock.tick(30)

main()
