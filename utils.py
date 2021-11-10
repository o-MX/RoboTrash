import pygame, sys

class TextoAnimado:
    def __init__(self,texto,tiempo):
        self.opacidad = 0
        self.milisegundos = 0
        self.tiempo = tiempo
        self.aumento = 10
        self.font = pygame.font.Font("./Assets/dogicapixel.ttf", 8) 
        self.text = self.font.render(texto, 0, (0, 0, 0)) 
        self.pos = (0, 0)

    def render(self, vp):
        vp.blit(self.text, (self.pos))

    def update(self, dt):
        self.text.set_alpha(self.opacidad)
        self.milisegundos += dt
        self.opacidad += self.aumento
        if self.milisegundos > self.tiempo:
            self.milisegundos = 0
            self.aumento = -self.aumento

class HealthIndicator:
    def __init___(self):
        self.sprite = None

class Heart:
    def __init__(self, status):
        self.set_health(status)

    def set_health(self, status):
        self.stats = status
