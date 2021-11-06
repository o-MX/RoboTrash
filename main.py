import sys, pygame
from typing import Text
import pantallas
import utils
pygame.init()

class Game:
    clock = pygame.time.Clock()
    screen_size = 800, 800 #800, 800
    bg = 0, 0, 0
    running = True
    display = None
    escene = None

    def run():
        Game.display = pygame.display.set_mode(Game.screen_size, pygame.RESIZABLE)
        Game.escene = pantallas.Inicio()
        while Game.running:
            Game.clock.tick(60)
            utils.Events.getEvents()
            if utils.Events.quit:
                Game.running = False
            Game.update()
            Game.render()

    def render():
        for e in pygame.event.get(pygame.VIDEORESIZE):
            Game.screen_size = e.size
        Game.display.fill(Game.bg)
        Game.escene.render()
        scaled = pygame.transform.scale(Game.escene.surface, Game.screen_size)
        Game.display.blit(scaled, (0, 0))
        pygame.display.flip()

    def update():
        dt = Game.clock.get_time()
        Game.escene.update(dt)
Game.run()
