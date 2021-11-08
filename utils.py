import pygame, sys

class Events:
    pulsadas = []
    quit = False

    def get():
        Events.pulsadas = pygame.event.get(pygame.KEYDOWN)
        Events.quit = pygame.event.peek(pygame.QUIT)

    def isKeyDown(key):
        for k in Events.pulsadas:
            if k.key == key:
                return True
        return False

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
