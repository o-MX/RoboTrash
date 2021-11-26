import pygame, sys
import utils
import eventhandler
import pantallas
import viewport
import assets
from robort import *

class Stage:
    def __init__(self, viewport, game):
        self.bg = (0, 0, 0)
        self.viewport = viewport
        self.surface = viewport.surface
        self.game = game

    def draw(self):
        self.surface.fill(self.bg)

    def update(self, dt):
        pass

class Inicio(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(196, 176), game)
        pygame.mixer.music.load('Assets/std_song.wav')
        pygame.mixer.music.play(3)
        self.texto_A = utils.TextoAnimado("Presione Z Para Iniciar", 900)
        self.texto_A.pos = (30, 100)
        self.cabeza = utils.MoveImg() #HEAD
        self.cabeza.coord_x = 75 #HEAD
        self.cabeza.coord_y = 120 #HEAD

    def draw(self):
        self.surface.blit(assets.bg_main, (0, 0))
        self.surface.blit(assets.title_sprite, (20, 20))
        self.texto_A.render(self.surface)
        self.cabeza.render(self.surface) #HEAD

    def update(self, dt):
        if(eventhandler.isKeyDown(pygame.K_z)):
            self.game.change_stage(Partida(self.game))
        self.texto_A.update(dt)
        self.cabeza.update()
