import pygame, sys

class Events:
    resize_event = []
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
