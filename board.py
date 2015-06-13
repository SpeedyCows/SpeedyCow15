__author__ = 'name'

import random
from object.dirt import Dirt


class Board:
    def __init__(self, screen):

        self.screen = screen

        self.screenWidth = 800
        self.screenHeight = 600
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
        self.board[boardX][boardY] = None

    def clearBoard(self):
        for x in range(self.horizontalBlocks):
            for y in range(self.verticalBlocks):
                self.clearBlock(x,y)

    def isEmpty(self, boardX, boardY):
        return self.board[boardX][boardY] == None

    def draw(self):
        for x in range(self.horizontalBlocks):
            for y in range(self.verticalBlocks):
                if not self.isEmpty(x,y):
                    self.board[x][y].draw(self.screen)

    def asList(self):
        list = []
        for row in self.board:
            for obj in row:
                if obj:
                    list += [obj]

        return list

    #private--------------------------------------

    def generate(self):
        chanceToChange = .3
        actor = [0,5]
        random.seed(0)
        direction = 0

        for x in range(300):
            #clear the board at the actor's position
            self.board[actor[0] % self.horizontalBlocks][actor[1] % self.verticalBlocks] = None

            #roll for changing the actor's direction
            if random.random() < chanceToChange:
                direction = random.randint(0,4)

            #move the actor in its current direction
            self.move(actor,direction)


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

