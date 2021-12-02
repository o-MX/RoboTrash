import math, assets, pygame
import events
from utils import *
from pygame import Rect, transform
from pygame.sprite import Sprite
from pygame.mixer import music
from stages import Stage

class Title(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.title
        self.rect = self.image.get_rect()
        self.rect.top = 20
        self.rect.centerx = 96

class Head(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.head
        self.rect = self.image.get_rect()
        self.rect.centerx = 96
        self.rect.bottom = 150
        self.time = 0
        self.duration = 2000
        self.offset = 10
    def update(self, dt):
        self.time += dt
        self.time %= self.duration
        t = self.time/self.duration
        ease = math.sin(2 * math.pi * t)
        self.rect.centerx = 96 + ease * self.offset 

class Text(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.dogicapixel.render(
            "Presiona Z para iniciar", True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (96, 100)
        self.time = 0
        self.duration = 1500
    def update(self, dt):
        self.time += dt
        self.time %= self.duration
        t = self.time / self.duration
        ease = 4 * t * (1 - t)
        self.image.set_alpha(ease * 255)

class Menu(Stage):
    def __init__(self, surface):
        Stage.__init__(self, assets.bg_main)
        surface.blit(self.bg, (0, 0))
        self.actors.add(Title(), Head(), Text())
        # music.load("./assets/std_song.wav")
        # music.play()
    def act(self, surface, dt):
        Stage.act(self, surface, dt)
        if events.isKeyDown(pygame.K_z):
            events.

