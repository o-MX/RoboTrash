import pygame, sys

from pygame.time import Clock
import utils


class Inicio:
    def __init__(self):
        self.size = 192, 176
        self.surface = pygame.Surface(self.size)
        self.bg = pygame.image.load("./Assets/main_bg.png") 
        self.title = pygame.image.load("./Assets/title.png") 
        self.personje = pygame.image.load("./Assets/cabeza.png") 
        self.personje = pygame.transform.scale(self.personje, (35,28)) 

    def render(self):
         self.surface.blit(self.bg, (0, 0)) 
         self.surface.blit(self.title, (20, 20)) 
         self.surface.blit(self.personje, (70,120)) 
        

    def update(self, dt):
        pass
class textoAnimado:
    def __init__(self):
        self.size = 192, 176
        self.opacidad = 0
        self.milisegundos = 0
        self.aumento = 10
        self.font = pygame.font.Font("./Assets/dogicapixel.ttf", 8) 
        self.text = self.font.render("Pulse Para Iniciar", 0, (0, 0, 0)) 
        
        
    def render(self):
        self.surface = pygame.Surface(self.size)
        self.surface.blit(self.text, (40, 95)) 
        

    def update(self, dt):
        self.milisegundos += dt
        self.opacidad += self.aumento
        self.opacidad = self.text.set_alpha(self.opacidad)
        if self.milisegundos > 1000:
            self.milisegundos = 0
            self.aumento = -self.aumento
