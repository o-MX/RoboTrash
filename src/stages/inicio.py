import pygame, sys
import eventhandler
import assets
from stages.base import Stage
from stages.partida import Partida

class TextoAnimado:
    def __init__(self, texto, tiempo):
        self.opacidad = 0
        self.milisegundos = 0
        self.tiempo = tiempo
        self.aumento = 10
        self.font = assets.dogicapixel_font
        self.text = self.font.render(texto, 0, (0, 0, 0))
        self.pos = (0, 0)
    def update(self, dt):
        self.text.set_alpha(self.opacidad)
        self.milisegundos += dt
        self.opacidad += self.aumento
        if self.milisegundos > self.tiempo:
            self.milisegundos = 0
            self.aumento = -self.aumento

class MoveImg:
    def __init__(self, x, y, img):
        self.pos = [x, y]
        self.moveimg = 0.1
        self.img = img
    def update(self, dt):
        if self.pos[0] > 80 or self.pos[0] < 70:
            self.moveimg = self.moveimg * -1
        self.pos[0] += self.moveimg

class Inicio(Stage):
    def __init__(self, viewport, game):
        Stage.__init__(self, viewport, game)
        pygame.mixer.music.load('assets/std_song.wav')
        pygame.mixer.music.play(3)
        self.texto_A = TextoAnimado("Presione Z Para Iniciar", 900)
        self.cabeza = MoveImg(75, 120, assets.head_sprite) 
    def act(self, dt):
        if(eventhandler.isKeyDown(pygame.K_z)):
            self.game.change_stage(Partida(self.viewport, self.game))
        self.texto_A.update(dt)
        self.cabeza.update(dt)
        self.render()
    def render(self):
        self.sf.blit(assets.bg_main, (0, 0))
        self.sf.blit(assets.title_sprite, (20, 20))
        self.sf.blit(self.texto_A.text, (30, 100))
        self.sf.blit(self.cabeza.img, self.cabeza.pos)

