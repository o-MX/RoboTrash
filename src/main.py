import sys, pygame
import eventhandler
import assets
import utils
from stages.inicio import Inicio
pygame.init()
eventhandler.init()
assets.load()

class RoboTrash:
    def __init__(self):
        self.size = (700, 600)
        self.bg = (0, 0, 0)
        self.running = True
        self.clock = pygame.time.Clock()
        # Creating the display
        flags = pygame.RESIZABLE
        self.display = pygame.display.set_mode(self.size, flags)
        # Finally creating a viewport
        self.viewport = utils.ViewportFit(self.display, (192, 176))
        self.stage = Inicio(self.viewport, self)
    def update(self):
        self.running = not eventhandler.quit
        self.clock.tick(60)
        dt = self.clock.get_time()
        self.stage.act(dt)
    def render(self):
        self.display.fill(self.bg)
        self.viewport.flip()
        pygame.display.flip()
    def change_stage(self, stage):
        self.stage = stage

game = RoboTrash()

while game.running:
    eventhandler.get()
    game.update()
    game.render()
