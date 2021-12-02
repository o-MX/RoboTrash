import pygame, random
import utils

class Player:


class Stage:
    def __init__(self, game):
        self.eventManager = game.eventManager
        self.bg = pygame.image.load("assets/gameplay.tga")
        self.items = pygame.sprite.Group()
        self.score = 0
        self.score_text = utils.Texto(str(self.score), 8, "pixelart.ttf", (0, 0, 0))
        self.score_label = utils.Texto("Score", 8, "pixelart.ttf", color=(0, 0, 0))
        self.time = utils.Texto("Score", 8, "pixelart.ttf", color=(0, 0, 0))
    def update(self, dt):
        self.items.update(dt)
    def draw(self, surface):
        surface.blit(self.bg, (0, 0))
        self.items.draw(surface)
    def start(self):
        self.items.add(self.score_text)
        self.items.add(self.score_label)
        self.score_text.rect.x = 134
        self.score_text.rect.y = 28
        self.score_label.rect.x = 134
        self.score_label.rect.y = 20
