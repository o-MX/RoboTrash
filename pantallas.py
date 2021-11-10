import pygame, sys
import utils
import eventhandler
import viewport
import assets

class Stage:
    def __init__(self, viewport, game):
        self.bg = (0, 0, 0)
        self.viewport = viewport
        self.surface = viewport.surface
        self.game = game

    def draw(self):
        self.surface.fill(self.bg)

    def update(self, dt):
        pass

class Inicio(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(196, 176), game)
        pygame.mixer.music.load('Assets/std_song.wav')
        # pygame.mixer.music.play(3)
        self.text = "Presiona Z para iniciar"

    def draw(self):
        self.surface.blit(assets.bg_main, (0, 0))
        self.surface.blit(assets.title_sprite, (20, 20))
        rendered_txt = assets.dogicapixel_font.render(self.text, False, 0)
        self.surface.blit(rendered_txt, (30, 100))
        self.surface.blit(assets.head_sprite, (75, 120))

    def update(self, dt):
        if(eventhandler.isKeyDown(pygame.K_z)):
            self.game.change_stage(Partida(self.game))

class Partida(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(196, 176), game)
        self.game_surface = pygame.Surface((80, 144))

    def draw(self):
        self.surface.blit(assets.bg_game, (0, 0))
        self.surface.blit(assets.head_sprite, (130, 130))

    def update(self, dt):
        pass
