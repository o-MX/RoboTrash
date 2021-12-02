import pygame

class Stage:
    played = True
    def __init__(self, game):
        self.eventManager = game.eventManager
        self.sprites = pygame.sprite.Group()
    def update(self, dt):
        self.sprites.update(dt)
    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.sprites.draw(surface)
    def start(self):
        if Stage.played:
            self.eventManager.change_scene("gameplay")

