import pygame
import common
from pygame.mixer import music

class Scene(common.Scene):
    bg = pygame.image.load("assets/gameover/bg.tga")
    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        music.load("assets/gameover/gameover.wav")
        music.play(-1)
