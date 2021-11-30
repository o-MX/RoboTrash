import src
import math
import assets
import pygame
from src import eventhandler
from pygame import Rect
from pygame.sprite import Sprite
from pygame import transform
from pygame.mixer import music
from src.models import Stage

class Text_GameOver(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.dogicapixel.render(
            "Game Over", True, src.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = src.CENTER_SCREEN
        self.rect.centery += 15
        self.time = 0
        self.duration = 1500
    def update(self, dt):
        self.time += dt
        self.time %= self.duration
        t = self.time / self.duration
        ease = 4 * t * (1 - t)
        self.image.set_alpha(ease * 255)

class GameOver(Stage):
    def __init__(self, surface):
        Stage.__init__(self)
        surface.fill((0, 0, 0))
        self.actors.add(Text_GameOver())
    def act(self, surface, dt):
        Stage.act(self, surface, dt)
        if(eventhandler.isKeyDown(pygame.K_z)):
            pass
