import pygame, sys
import utils

class Viewport:
    def __init__(self, width, height):
        self.size = (width, height)
        self.surface = pygame.Surface(self.size)
        self.ratio = width / height

    def flip(self, dest):
        return self.surface

class Fit(Viewport):
    def __init__(self, width, height, center = True):
        Viewport.__init__(self, width, height)

    def flip(self, dest):
        dest_size = dest.get_size()
        dest_ratio = dest_size[0] / dest_size[1]
        scale_rect = pygame.Rect(0, 0, 0, 0)

        if dest_ratio > self.ratio:
            scale_rect.width = self.size[0] * dest_size[1] / self.size[1]
            scale_rect.height = dest_size[1]
        else:
            scale_rect.width = dest_size[0]
            scale_rect.height = self.size[1] * dest_size[0] / self.size[0]

        scale_rect.x = (dest_size[0] - scale_rect.width) / 2
        scale_rect.y = (dest_size[1] - scale_rect.height) / 2

        scaled = pygame.transform.scale(self.surface,
            (scale_rect.width, scale_rect.height))
        dest.blit(scaled, (scale_rect.x, scale_rect.y))
