from object import Object
import pygame

class Dirt(Object):  # represents the water, not the game
    def __init__(self, dimension):
        """ The constructor of the class """
        super(Dirt, self).__init__(dimension)

        self.life = 4

	# Option 1 - Loads fast
        #self.red = 68
        #self.green = 26
        #self.blue = 26
        #self.width = 0
    
        #self.empty = False

	# Option 2 - Loads slow
	#self.image = pygame.image.load('images/dirt3.png')

	# Option 3 - Loads ok, but images quality reduced
        self.image = pygame.image.load('images/dirt3.png')
        #self.image = pygame.transform.scale(self.image, (dimension, dimension))

    def collide(self, object):
        return
        #if type(object).__name__ == 'Player_Ant':
        #self.empty = True

    def isMovable(self):
        return False
