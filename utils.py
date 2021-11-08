import pygame, sys

class TextoAnimado:
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

class HealthIndicator:
    def __init___(self):
        self.sprite = None

class Heart:
    def __init__(self, status):
        self.set_health(status)

    def set_health(self, status):
        self.stats = status
