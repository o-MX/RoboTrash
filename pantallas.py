import pygame, sys
import utils
import eventhandler
import viewport
import assets

class Stage:
    def __init__(self, viewport, game):
        self.bg = (0, 0, 0)
        self.viewport = viewport
        self.surface = viewport.surface
        self.game = game

    def draw(self, sf):
        sf.fill(self.bg)

    def update(self, dt):
        pass

class Inicio(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(196, 176), game)
        pygame.mixer.music.load('Assets/std_song.wav')
        pygame.mixer.music.play(3)

    def draw(self):
        self.surface.blit(assets.bg_main, (0, 0))
        # self.surface.blit(self.text, (80, 100))
        # self.surface.blit(self.title, (20, 20))
        # self.surface.blit(self.personje, (70,120))

    def update(self, dt):
        if(eventhandler.isKeyDown(pygame.K_RETURN)):
            self.game.change_stage(Partida(self.game))

class Partida(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(196, 176), game)
        self.bg = pygame.image.load("./Assets/game_bg.tga")

    def draw(self):
        self.surface.blit(self.bg, (0, 0))

    def update(self, dt):
        pass
