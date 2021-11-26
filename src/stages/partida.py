import pygame, sys
import assets
from stages.base import Stage

class Health:
    def __init__(self, lives):
        self.health = lives
        self.hearts = []
        for i in range(lives):
            self.hearts.append(assets.hearts_sprite.subsurface(0, 0, 12, 11))
    def addHealth(self, quant):

    
class Partida(Stage):
    def __init__(self, viewport, game):
        Stage.__init__(self, viewport, game)
        self.health = Health(3)
    def render(self):
        self.sf.blit(assets.bg_game, (0, 0))
        self.sf.blit(assets.head_sprite, (130, 130))
        for i, h in enumerate(self.health.hearts):
            self.sf.blit(h, (130 + 12 * i + 2 * i, 90))
    def act(self, dt):
        self.render()
