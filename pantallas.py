import pygame, sys
import utils
import eventhandler
import viewport

class Stage:
    def __init__(self, viewport, game):
        self.bg = (0, 0, 0)
        self.viewport = viewport
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
        self.bg = pygame.image.load("./Assets/main_bg.tga")
        self.title = pygame.image.load("./Assets/title.tga")
        self.font = pygame.font.Font("./Assets/dogicapixel.ttf", 10)
        self.text = self.font.render("Iniciar", False, (0, 0, 0))
        self.personje = pygame.image.load("./Assets/cabeza.tga") 
        self.personje = pygame.transform.scale(self.personje, (35,28)) 

    def draw(self):
        self.viewport.surface.blit(self.bg, (0, 0))
        self.viewport.surface.blit(self.text, (80, 100))
        self.viewport.surface.blit(self.title, (20, 20))
        self.viewport.surface.blit(self.personje, (70,120))

    def update(self, dt):
        if(eventhandler.isKeyDown(pygame.K_RETURN)):
            self.game.change_stage(Partida(self.game))

class Partida(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(196, 176), game)
        self.bg = pygame.image.load("./Assets/game_bg.tga")
        self.cabeza = pygame.image.load("./Assets/cabeza.tga")

    def draw(self):
        self.viewport.surface.blit(self.bg, (0, 0))
        self.viewport.surface.blit(self.cabeza, (130, 130))
        # self.viewport.blit(self.game_surface, (90, 14))

    def update(self, dt):
        pass
