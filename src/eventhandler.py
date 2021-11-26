import pygame, sys
from pygame import event

_pressed = []
quit = False

def init():
    event.set_blocked(None)
    event.set_allowed([
        pygame.KEYDOWN,
        pygame.KEYUP,
        pygame.VIDEORESIZE,
        pygame.JOYBUTTONDOWN,
        pygame.JOYBUTTONUP,
        pygame.QUIT
    ])

def get():
    global _pressed, quit
    _pressed = event.get(pygame.KEYDOWN)
    quit = event.peek(pygame.QUIT)

def isKeyDown(key):
    global _pressed
    for k in _pressed:
        if k.key == key:
            return True
    return False

