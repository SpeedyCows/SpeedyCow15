from eventmanager import EventManager, SoundEffectEvent
import pygame, pygame.mixer
import random

class SoundManager:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener( self )
        self.list = ['sounds/song1.wav', 'sounds/song2.wav', 'sounds/song3.wav', 'sounds/song4.wav', 'sounds/song5.wav', 'sounds/song6.wav']
        pygame.mixer.init()
        self.index = random.randint(0, len(self.list) - 1)
        self.sound = pygame.mixer.Sound(self.list[self.index])
        self.channel = self.sound.play()
        self.channel.set_endevent
        
        
    def Notify(self, event):
        if isinstance( event, SoundEffectEvent ):
            print event.name
            sound = pygame.mixer.Sound(event.filename)
            sound.play()
    
    
    def PlayNext(self):
        self.index = (self.index + 1) % len(self.list)
        self.sound = pygame.mixer.Sound(self.list[self.index])
        self.sound.play()

            