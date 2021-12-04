import pygame
import common

class Scene(common.Scene):
    bg = pygame.image.load("assets/gameplay/gameplay.tga")
    def __init__(self):
        super().__init__((160, 160), common.WHITE)
        self.bg = Scene.bg
        self.surface.blit(self.bg, (0, 0))

    def update(self, game):
        super().update(game)

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
