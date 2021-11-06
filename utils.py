import pygame, sys

class Events:
    resize_event = []
    pulsadas = []
    quit = False

    def get():
        Events.pulsadas = pygame.event.get(pygame.KEYDOWN)
        Events.quit = pygame.event.peek(pygame.QUIT)

    def isKeyDown(key):
        for k in Events.pulsadas:
            if k.key == key:
                return True
        return False
