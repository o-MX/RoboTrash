import pygame, sys

class Events:
    pulsadas = []
    quit = False

    def getEvents():
        Events.pulsadas = pygame.event.get(pygame.KEYDOWN)
        Events.quit = pygame.event.peek(pygame.QUIT)
        if pygame.event.

    def isKeyDown(key):
        for k in Events.pulsadas:
            if k.key == key:
                return True
        return False
