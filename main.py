import pygame, os, time

from object.object import *
from object.player_ant import *
from object.water import Water
from object.dirt import Dirt
from object.crazyant import CrazyAnt
from object.queen import Queen
from board import Board
from random import Random

from object.pyganim import *
PLAYER_SIZE = 80
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
        screen.blit(pygame.font.Font(None, 50).render("GAME OVER!", True, (255, 255, 255)), (275, 250))
        if ant.score == 0:
           screen.blit(pygame.font.Font(None, 25).render("You Lose", True, (255, 255, 255)), (325, 300))
        else:
           screen.blit(pygame.font.Font(None, 25).render("Your score is " + str(ant.score), True, (255, 255, 255)), (325, 300))
        

def processPYGame(ant, keycount):
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit() # quit the screen
           sys.exit(1)
        elif event.type == pygame.KEYDOWN:
           #need to count key down so that we can track when they are released
           keycount += 1
           ant.handle_key(event)
        elif event.type == pygame.KEYUP:
            #only pause if num of key down is now 0
            keycount -= 1
            if keycount <= 0:
                keycount = 0
                ant.pause_ani()
        elif event.type == pygame.MOUSEMOTION:
            ant.handle_mouse(event)

def main():
    pygame.init()
    rand = Random()
    background = pygame.image.load("images/grass.jpg")
    backgroundRect = background.get_rect()
    screen = pygame.display.set_mode((800, 600))
    enemyAnts = []
    clock = pygame.time.Clock()
    ant = Player_Ant(SQUARE_SIZE)
    crazyAnt = CrazyAnt(SQUARE_SIZE, ant, 'e')
    crazyAnt.setPos(500, 500)
    enemyAnts.append(crazyAnt)
    #Create the board
    board = Board(screen)
    movableObjects, staticObjects = board.getObjects()
    movableObjects += [ant]
    movableObjects.append(crazyAnt)

    queen = Queen(SQUARE_SIZE)
    queen.setPos(420, 420)
    movableObjects.append(queen)

    keycount = 0
    started = False
    numberOfCrazyAnts = 1
    while True:
        t = time.clock()
        if(t/10 > numberOfCrazyAnts):
            crazyAnt = CrazyAnt(SQUARE_SIZE, ant, 'e')
            randomX = rand.randint(20, 500)
            randomY = rand.randint(20, 500)
            crazyAnt.setPos(randomX, randomY)
            numberOfCrazyAnts += 1
            movableObjects.append(crazyAnt)
            enemyAnts.append(crazyAnt)
        screen.blit(background, backgroundRect)
        if not started:
            font = pygame.font.Font(None, 50)
            mes = font.render("Press <ENTER> to Start", True, (255, 0, 0))
            screen.blit(mes, (200, 250))
            pygame.display.update() # update the screen
            while True:
                processPYGame(ant, keycount)
                key = pygame.key.get_pressed()
                if key[pygame.K_RETURN]:
                    started = True
                    break
                if key[pygame.K_ESCAPE]:
                    sys.exit(0)

        processPYGame(ant, keycount)

        ant.inBetweenLoops()
        ant.update_pos()
        for object in movableObjects:
            object.inBetweenLoops()

        queen.move()

        for staticObject in staticObjects:
            for movableObject in movableObjects:
                if (movableObject.check_collision(staticObject)):

                    #collide both ways
                    movableObject.collide(staticObject)
                    staticObject.collide(movableObject)

            if (staticObject.delete == True):
                staticObjects.remove(staticObject)

        for object3 in staticObjects:
            if (ant.check_collision(object3)):
                ant.collide(object3)
                object3.collide(ant)
                if (object3.delete):
                    staticObjects.remove(object3)
                    
        for object3 in movableObjects :
            if (ant.check_collision(object3)):
                ant.collide(object3)
                object3.collide(ant)
                if (object3.delete):
                    movableObjects.remove(object3)
                
        for object3 in movableObjects:
            if (object3.delete == True):
                movableObjects.remove(object3)                    
            
        #collide movable objects against each other
        for object3 in movableObjects:
            for object4 in movableObjects:
                if (object3 != object4):
                    if (object3.check_collision(object4)):
                        object3.collide(object4)
                for crazyAnt in enemyAnts:
                    crazyAnt.searchForPlayer()

        #draw all objects
        for obj in staticObjects + movableObjects:
            obj.draw(screen)
            
        ant.draw(screen)
        
        HUD(screen, ant)

        pygame.display.update() # update the screen

        clock.tick(30)

main()
