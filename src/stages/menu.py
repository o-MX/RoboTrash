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

class Title(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.title
        self.rect = self.image.get_rect()
        self.rect.x = (192 - self.rect.width)/2
        self.rect.y = (176 - self.rect.height)/2
        self.rect.y -= 35

class Head(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.head
        self.time = 0
        self.rect = self.image.get_rect()
        self.rect.center = src.CENTER_SCREEN
        self.rect.centery += 50
        self.duration = 2000
        self.offset = 10
    def update(self, dt):
        self.time += dt
        self.time %= self.duration
        t = self.time/self.duration
        ease = math.sin(2 * math.pi * t)
        self.rect.centerx = src.CENTER_SCREEN[0] + ease * self.offset 

class Text(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.dogicapixel.render(
            "Presiona Z para iniciar", True, src.BLACK)
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

class Menu(Stage):
    def __init__(self):
        Stage.__init__(self)
        self.bg = assets.bg_main
        self.actors.add(Title())
        self.actors.add(Head())
        self.actors.add(Text())
        music.load("./assets/std_song.wav")
        music.play()
        
    def act(self, surface, dt):
        surface.blit(self.bg, self.bg.get_rect())
        Stage.act(self, surface, dt)
        if eventhandler.isKeyDown(pygame.K_z):
            print("Hola")
