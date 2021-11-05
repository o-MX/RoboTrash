import sys, pygame
import pantallas
import utils
pygame.init()

class Game:
    clock = pygame.time.Clock()
    size = 800, 800
    ratio = 0
    bg = 0, 0, 0
    running = True
    display = None
    escene = None

    def run():
        Game.display = pygame.display.set_mode(Game.size, pygame.RESIZABLE)
        Game.escene = pantallas.Inicio()
        while Game.running:
            Game.clock.tick(60)
            utils.Events.getEvents()
            if utils.Events.quit:
                Game.running = False
            Game.update()
            Game.render()

    def render():
        Game.display.fill(Game.bg)
        pygame.display.flip()

    def update():
        dt = Game.clock.get_time()
        Game.escene.update(dt)

Game.run()
