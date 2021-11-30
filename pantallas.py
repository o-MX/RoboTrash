import pygame, sys
import utils
import eventhandler
import pantallas
import viewport
import assets
from robort import *

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

        self.texto_A = utils.TextoAnimado("Presione Z Para Iniciar", 900)
        self.texto_A.pos = (30, 100)
        self.cabeza = utils.MoveImg() #HEAD
        self.cabeza.coord_x = 75 #HEAD
        self.cabeza.coord_y = 120 #HEAD

    def draw(self):
        self.surface.blit(assets.bg_main, (0, 0))
        self.surface.blit(assets.title_sprite, (20, 20))
        self.texto_A.render(self.surface)
        self.cabeza.render(self.surface) #HEAD

    def update(self, dt):
        if(eventhandler.isKeyDown(pygame.K_z)):
            self.game.change_stage(Partida(self.game))
            pygame.mixer.music.set_volume(0.0)
        self.texto_A.update(dt)
        self.cabeza.update()

class Partida(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(192, 176), game)
        self.game_surface = pygame.Surface((80, 144))
        self.robort = Robort(self.game_surface.get_height() - 15)
        self.health_indicator = utils.HealthIndicator()

    def draw(self):
        self.surface.blit(assets.bg_game, (0, 0))
        self.surface.blit(assets.head_sprite, (130, 130))
        self.surface.blit(self.health_indicator.surface, (135, 100))
        self.game_surface.fill((255, 255, 255))
        self.game_surface.blit(self.robort.sprite, self.robort.pos)
        self.surface.blit(self.game_surface, (32, 16))

    def update(self, dt):
        if eventhandler.isKeyDown(pygame.K_z):
            self.robort.rotate()
            self.health_indicator.take_damage(0.5)
        if eventhandler.isKeyDown(pygame.K_RIGHT):
            self.robort.move_right()
        elif eventhandler.isKeyDown(pygame.K_LEFT):
            self.robort.move_left()
        if self.health_indicator.health <= 0:
            self.game.change_stage(pantallas.GameOver(self.game))


class GameOver(Stage):
    def __init__(self, game):
        Stage.__init__(self, viewport.Fit(196, 176), game)
        self.texto_A = utils.TextoAnimado("Game Over", 900)
        self.texto_A.pos = (30, 30)
        self.exit = utils.MoveImg() #HEAD
        self.exit.coord_x = 55 #HEAD
        self.exit.coord_y = 100 #HEAD
        self.retry = utils.MoveImg() #HEAD
        self.retry.coord_x = 75 #HEAD
        self.retry.coord_y = 120 #HEAD

    def draw(self):
        self.texto_A = utils.TextoAnimado("Game Over", 900)
        self.texto_A.pos = (30, 30)
        self.surface.blit(assets.bg_main, (0, 0))
        self.retry.render(self.surface)
        self.exit.render(self.surface)

    def update(self, dt):
        if(eventhandler.isKeyDown(pygame.K_z)):
            self.game.change_stage(Partida(self.game))
        self.texto_A.update(dt)
        self.exit.update()
        self.retry.update()

    def exit(self,game):
        self.retry
        self.exit

