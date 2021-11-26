import pygame, sys

_pressed = []
quit = False

def init():
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([
        pygame.KEYDOWN,
        pygame.KEYUP,
        pygame.VIDEORESIZE,
        pygame.JOYBUTTONDOWN,
        pygame.JOYBUTTONUP,
        pygame.QUIT
    ])

def get():
    global _pressed, quit
    _pressed = pygame.event.get(pygame.KEYDOWN)
    quit = pygame.event.peek(pygame.QUIT)

def isKeyDown(key):
    global _pressed
    for k in _pressed:
        if k.key == key:
            return True
    return False

