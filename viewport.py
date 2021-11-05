import pygame, sys
import utils

class Fit:
    def __init__(self, pygame.Surface dest, tuple size):
        self.dest = dest
        self.rect = pygame.Rect((0, 0), size)
        self.surface = pygame.Surface(size)
        self.ratio = self.rect.width / self.rect.height

    def flip(self):
        scaled = pygame.transform.scale(self.surface, size)
        self.dest.blit(scaled, self.rect)
