import pygame, os, time, copy

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
BLOCK_SIZE = 40
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)

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
        screen.blit(pygame.font.Font(None, 25).render("Press <SPACE> to try again", True, (255, 255, 255)), (275, 450))
        pygame.display.update()
        keycount = 0
        while True:
            processPYGame(ant, keycount)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
               return False
            if key[pygame.K_ESCAPE]:
               sys.exit(0)
    return True

def main():
    pygame.init()
    rand = Random()

    #make background dirt
    topdirt = pygame.image.load("images/dirt1.png")
    topdirt = pygame.transform.scale(topdirt, (BLOCK_SIZE, BLOCK_SIZE))
    backdirt = pygame.image.load("images/dirt2.png")
    backdirt = pygame.transform.scale(backdirt, (BLOCK_SIZE, BLOCK_SIZE))
    background = pygame.image.load("images/dirt.jpg")
    for b_x in range(0, 800, BLOCK_SIZE):
        background.blit(topdirt, (b_x, 0))
        for b_y in range(BLOCK_SIZE, 600, BLOCK_SIZE):
            background.blit(backdirt, (b_x, b_y))

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

    started = False
    keycount = 0
    numberOfCrazyAnts = 1

    scoreTimer = time.clock()

    logo = pygame.image.load('images/sugar-ant.png')
    font = pygame.font.Font(None, 50)
    mes = font.render("Press <ENTER> to Start", True, (255, 0, 0))
    gamename = font.render("Crazy Ants!", True, (0, 255, 0))

    while True:
        t = time.clock()
        if(t/20 > numberOfCrazyAnts):
            if(t < 40):
                spawnCrazyAnt(numberOfCrazyAnts, rand, enemyAnts, movableObjects, ant, 'e')
                numberOfCrazyAnts += 1
            elif(t < 40 and t >= 20):
                spawnCrazyAnt(numberOfCrazyAnts, rand, enemyAnts, movableObjects, ant, 'm')
                numberOfCrazyAnts += 1
            else:
                spawnCrazyAnt(numberOfCrazyAnts, rand, enemyAnts, movableObjects, ant, 'h')
                numberOfCrazyAnts += 1
        if (t - scoreTimer) > 1:
            ant.score += 1
            scoreTimer = t
        screen.blit(background, backgroundRect)
        if not started:
            screen.blit(mes, (200, 250))

            ant.score = ant.initial_score
            ant.lives = ant.initial_lives
            ant.leaves = ant.initial_leaves
            ant.sugar = ant.initial_sugar

            screen.blit(gamename, (300, 350))
            screen.blit(logo, (380, 400))

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
                    for cA in enemyAnts:
                        cA.searchForPlayer()

        #draw all objects
        for obj in staticObjects + movableObjects:
            obj.draw(screen)
            
        ant.draw(screen)
        
        started = HUD(screen, ant)

        pygame.display.update() # update the screen

        clock.tick(20)

def spawnCrazyAnt(numberOfCrazyAnts, rand, enemyAnts, movableObjects, ant, arg ):
    crazyAnt = copy.copy(CrazyAnt(SQUARE_SIZE, ant, arg))
    randomX = rand.randint(100, 500)
    randomY = rand.randint(100, 500)
    if(randomX != ant.x and randomY != ant.y):
        crazyAnt.setPos(randomX, randomY)
        movableObjects.append(crazyAnt)
        enemyAnts.append(crazyAnt)
        crazyAnt.aggresiveSearchForPlayer()

if __name__=='__main__':main()
