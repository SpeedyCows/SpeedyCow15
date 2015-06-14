__author__ = 'name'

import random
from object.dirt import Dirt
from object.sugar import Sugar
from object.block import Boulder
from object.water import Water
from object.leaf import Leaf
from object.fire import Fire


class Board:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    
    def __init__(self, screen, evManager):

        self.screen = screen

        # Event manager reference to give to objects requiring events
        self.evManager = evManager
        
        self.screenWidth = Board.SCREEN_WIDTH
        self.screenHeight = Board.SCREEN_HEIGHT
        self.squareSize = 20

        self.horizontalBlocks = self.screenWidth / self.squareSize
        self.verticalBlocks = self.screenHeight / self.squareSize

        #init the board
        self.board = [[None for x in range(self.verticalBlocks)] for x in range(self.horizontalBlocks)]

        #fill all with dirt
        for x in range(self.horizontalBlocks):
            for y in range(self.verticalBlocks):
                self.setBlock(Dirt(self.squareSize), x, y)

        #clear paths in the board and fill with stuff
        self.generate()

    def setBlock(self, object, boardX, boardY):
        #set the object's location on the screen
        object.setPos(self.toScreenX(boardX), self.toScreenY(boardY))

        #place it in the board
        self.board[boardX][boardY] = object

    def clearBlock(self, boardX, boardY):
        if self.inRange(boardX, boardY):
            self.board[boardX][boardY] = None

    def clearBoard(self):
        for x in range(self.horizontalBlocks):
            for y in range(self.verticalBlocks):
                self.clearBlock(x,y)

    def isEmpty(self, boardX, boardY):
        if not self.inRange(boardX, boardY):
            return False
        return self.board[boardX][boardY] == None

    def inRange(self, x, y):
        return x > 0 and y > 0 and x < self.horizontalBlocks and y < self.verticalBlocks

    def draw(self):
        for x in range(self.horizontalBlocks):
            for y in range(self.verticalBlocks):
                if not self.isEmpty(x,y):
                    self.board[x][y].draw(self.screen)

    def getObjects(self):
        movables = []
        statics = []
        for row in self.board:
            for obj in row:
                if obj:
                    if obj.isMovable():
                        movables += [obj]
                    else:
                        statics += [obj]

        return movables, statics

    #private--------------------------------------

    def generate(self):
        chanceToChange = .3
        actor = [0,0]
        direction = 0

        for x in range(300):
            #clear the board at the actor's position
            self.clearSquares(actor)

            #roll for changing the actor's direction
            if random.random() < chanceToChange:
                direction = random.randint(0,4)

            #move the actor in its current direction
            self.move(actor,direction)

        #add static objects in or adjacent to open spaces
        for x in range(self.horizontalBlocks):
            for y in range(self.verticalBlocks):
                if random.random() < .05 and self.spaceClear(x, y):
                    itemNum = random.randint(0,4)
                    if itemNum == 0:
                        self.setBlock(Sugar(self.squareSize), x, y)
                    elif itemNum == 1:
                        self.setBlock(Boulder(self.squareSize), x, y)
                    elif itemNum == 2:
                        self.setBlock(Water(self.squareSize, Board.SCREEN_WIDTH, Board.SCREEN_HEIGHT), x, y)
                    elif itemNum == 3:
                        self.setBlock(Leaf(self.squareSize), x, y)
                    elif itemNum == 4:
                        self.setBlock(Fire(self.squareSize * 2, self.evManager), x, y)

    def clearSquares(self, actor):
        self.board[actor[0] % self.horizontalBlocks][actor[1] % self.verticalBlocks] = None
        self.board[actor[0] % self.horizontalBlocks][(actor[1]+1) % self.verticalBlocks] = None
        self.board[(actor[0]+1) % self.horizontalBlocks][actor[1] % self.verticalBlocks] = None
        self.board[(actor[0]+1) % self.horizontalBlocks][(actor[1]+1) % self.verticalBlocks] = None

    def toScreenX(self, boardX):
        return (self.screenWidth / self.horizontalBlocks) * boardX

    def toScreenY(self, boardY):
        return (self.screenHeight / self.verticalBlocks) * boardY

    def north(self, actor):
        actor[1] -= 1

    def south(self, actor):
        actor[1] += 1

    def east(self, actor):
        actor[0] += 1

    def west(self, actor):
        actor[0] -= 1

    def move(self, actor, direction):
        if direction == 0:
            self.north(actor)
        elif direction == 1:
            self.east(actor)
        elif direction == 2:
            self.south(actor)
        else:
            self.west(actor)

    #why do things have to be different sizes?
    def spaceClear(self, x, y):
        return self.isEmpty(x, y) and \
               self.isEmpty(x+1, y) and \
               self.isEmpty(x, y+1) and \
               self.isEmpty(x+1, y+1)


