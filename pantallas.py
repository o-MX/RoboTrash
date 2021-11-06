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

    def draw(self, vp):
        vp.blit(self.bg, (0, 0))
        vp.blit(self.text, (80, 100))
        vp.blit(self.title, (20, 20))

    def update(self, dt):
        if(utils.Events.isKeyDown(pygame.K_RETURN)):
            self.game.changeStage(Inicio(self.game))
