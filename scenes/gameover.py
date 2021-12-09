import pygame
from pygame.constants import K_RIGHT
import common
from pygame.mixer import music

class Cursor(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("assets/gameover/cursor.tga")
        self.rect = self.image.get_rect()
        self.rect.x = 38
        self.rect.top = 130

class Scene(common.Scene):
    bg = pygame.image.load("assets/gameover/bg.tga")

    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        self._continue = True
        self.cursor = Cursor(self.group)
        music.load("assets/gameover/gameover.wav")
        music.play(-1)

    def update(self, game):
        super().update(game)
        if game.events.isKeyDown(pygame.K_z):
            if self._continue:
                game.change_scene("gameplay")
            else:
                game.change_scene("main")
        if game.events.isKeyDown(pygame.K_LEFT):
            self.cursor.rect.x = 38
            self._continue = True
        elif game.events.isKeyDown(pygame.K_RIGHT):
            self.cursor.rect.x = 100
            self._continue = False
