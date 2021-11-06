import pygame, sys
import utils

class Inicio:
    def __init__(self, game):
        pygame.mixer.music.load('Assets/std_song.wav')
        pygame.mixer.music.play(3)
        self.game = game
        self.bg = pygame.image.load("./Assets/main_bg.png")
        self.title = pygame.image.load("./Assets/title.png")
        self.font = pygame.font.Font("./Assets/dogicapixel.ttf", 10)
        self.text = self.font.render("Iniciar", False, (0, 0, 0))
        self.personje = pygame.image.load("./Assets/cabeza.png") 
        self.personje = pygame.transform.scale(self.personje, (35,28)) 
        
    def draw(self, vp):
        vp.blit(self.bg, (0, 0))
        vp.blit(self.text, (80, 100))
        vp.blit(self.title, (20, 20))
        vp.blit(self.personje, (70,120)) 


    def update(self, dt):
        if(utils.Events.isKeyDown(pygame.K_RETURN)):
            self.game.changeStage(Inicio(self.game))

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