from eventmanager import EventManager, SoundEffectEvent
import pygame, pygame.mixer

class SoundManager:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener( self )
        self.sound = None
        
    def Notify(self, event):
        if isinstance( event, SoundEffectEvent ):
            print event.name
            self.sound = pygame.mixer.Sound(event.filename)
            self.sound.play()
            


            