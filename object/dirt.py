from object import Object
import pygame

class Dirt(Object):  # represents the water, not the game
    def __init__(self, dimension):
        """ The constructor of the class """
        super(Dirt, self).__init__(dimension)

	# Option 1 - Loads fast
	self.red = 68
	self.green = 26
	self.blue = 26
	self.width = 0

	# Option 2 - Loads slow
	#self.image = pygame.image.load('images/dirt.jpg')

	# Option 3 - Loads ok, but images quality reduced
        #self.image = pygame.image.load('images/dirt_resized.jpg')
        #self.image = pygame.transform.scale(self.image, (dimension, dimension))
