import pygame, sys
import utils


class Inicio:
    def __init__(self):
        self.size = 192, 176
        self.surface = pygame.Surface(self.size)
        self.bg = pygame.image.load("./Assets/TITLE_BG.png")

    def render(self):
        self.surface.blit(self.bg, (0, 0))

    def update(self, dt):
        pass
