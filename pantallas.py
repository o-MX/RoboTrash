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
            self.game.changeStage(Partida(self.game))

class Partida:
    def __init__(self, game):
        self.game = game
        self.bg = pygame.image.load("./Assets/game_bg.png")
        self.cabeza = pygame.image.load("./Assets/cabeza.png")
        self.tileset = pygame.image.load("./Assets/game_tileset.png")
        self.botes = pygame.image.load("./Assets/trash_cans.png")
        self.basuras = pygame.image.load("./Assets/trash.png")

        self.game_surface = pygame.Surface((80, 140))
        self.stage = pygame.Surface((192, 176))

    def draw(self, vp):
        vp.blit(self.bg, (0, 0))
        vp.blit(self.cabeza, (90, 100))
        vp.blit(self.game_surface, (90, 14))

    def update(self, dt):
        pass
