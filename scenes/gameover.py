import pygame

class Stage:
    def __init__(self, game):
        self.eventManager = game.eventManager
        self.bg = pygame.image.load("assets/bg2.tga")
    def update(self, dt):
        pass
    def draw(self, surface):
        pass
