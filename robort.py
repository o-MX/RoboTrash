import pygame, sys
import assets
import eventhandler

class Robort:
    def __init__(self, y, orienta):
        self.rect = pygame.Rect(0, y, 26, 15)
