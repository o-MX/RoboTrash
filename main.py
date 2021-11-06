import sys, pygame
from typing import Text
import utils as u
import viewport as v
import pantallas as p
pygame.init()

class Game:
    clock = pygame.time.Clock()
    size = 800, 800
    display = None
    viewport = None
    stage = None

    def run():
        while not u.Events.quit:
            Game.clock.tick(60)
            u.Events.get()
            Game.update()
            Game.render()

    def render():
        Game.stage.draw(Game.viewport.surface)
        Game.viewport.flip(Game.display)
        pygame.display.flip()

    def update():
        dt = Game.clock.get_time()
        Game.stage.update(dt)

    def changeStage(stage):
        Game.stage = stage

Game.display = pygame.display.set_mode(Game.size, pygame.RESIZABLE)
Game.viewport = v.Fit(192, 176)
Game.stage = p.Inicio(Game)
# Icono y Titulo
icono = pygame.image.load("Assets/cabeza.png")
pygame.display.set_caption("RoboTrash")
pygame.display.set_icon(icono)

Game.run()
