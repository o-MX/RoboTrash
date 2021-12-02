import pygame

keyDown = []

def handle():
    global keyDown
    keyDown = pygame.event.get(pygame.KEYDOWN)

def is_key_down(code):
    for k in keyDown:
        if k.key == code:
            return True
    return False

