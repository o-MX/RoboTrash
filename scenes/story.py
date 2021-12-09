import pygame
import common
from pygame.mixer import music

class Scene(common.Scene):
    visited = False
    bg = pygame.image.load("assets/story/bg.tga")

    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        music.load("assets/story/story.wav")
        music.play(-1)
        self.time = 0
    
    def update(self, game):
        self.time += game.clock.get_time()
        if Scene.visited:
            game.change_scene("gameplay")
        if self.time > 10000:
            game.change_scene("gameplay")
            self.visited = True
