import pygame

class Stage:
    def __init__(self, game):
        self.eventManager = game.eventManager
    def update(self, dt):
        self.eventManager.change_scene("main")
    def draw(self, surface):
        pass
