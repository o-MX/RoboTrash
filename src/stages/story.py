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

class Story(Stage):
    def __init__(self, surface):
        Stage.__init__(self)
        self.bg = assets.bg_main
        surface.blit(self.bg, (0, 0))
        self.actors.add(Title())
        self.actors.add(Head())
        self.actors.add(Text())
        music.load("./assets/std_song.wav")
        music.play()
    def act(self, surface, dt):
        Stage.act(self, surface, dt)
        if eventhandler.isKeyDown(pygame.K_z):
            music.stop()
