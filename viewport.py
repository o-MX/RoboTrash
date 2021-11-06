import pygame, sys
import utils

class Fit:
    def __init__(self, width, height):
        self.size = (width, height)
        self.surface = pygame.Surface(self.size)
        self.ratio = self.surface.get_width() / self.surface.get_height()

    def flip(self, dest):
        s = dest.get_size()
        rs = s[0] / s[1]
        pos = pygame.Rect(0, 0, 0, 0)

        if rs > self.ratio:
            pos.width, pos.height = self.size[0] * s[1] / self.size[1], s[1]
        else:
            pos.width, pos.height = s[0], self.size[1] * s[0] / self.size[0]

        pos.x, pos.y = (s[0] - pos.width) / 2, (s[1] - pos.height) / 2

        scaled = pygame.transform.scale(self.surface, (pos.width, pos.height))
        dest.blit(scaled, pos)
