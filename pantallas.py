import pygame, sys
import utils


class Inicio:
    def __init__(self):
        #Adair
        pygame.mixer.music.load('Assets/std_song.wav')
        pygame.mixer.music.play(3)
        self.size = 192, 176
        self.surface = pygame.Surface(self.size)
        self.bg = pygame.image.load("./Assets/main_bg.png")
        self.title = pygame.image.load("./Assets/title.png")
        self.font = pygame.font.Font("./Assets/dogicapixel.ttf", 8)
        self.text = self.font.render("Iniciar", 0, (0, 0, 0))

    def render(self):
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.text, (40, 100))
        self.surface.blit(self.title, (20, 20))

    def update(self, dt):
        pass
