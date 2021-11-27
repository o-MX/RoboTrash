import sys, pygame
from typing import Text
import pantallas
import eventhandler
import assets
pygame.init()
eventhandler.init()
assets.load()

class RoboTrash:
    def __init__(self):
        self.stage = pantallas.Inicio(self)
        self.size = (700, 600)
        self.bg = (0, 0, 0)
        self.running = True
        self.clock = pygame.time.Clock()

        flags = pygame.RESIZABLE
        self.display = pygame.display.set_mode(self.size, flags)

    def update(self):
        self.running = not eventhandler.quit
        self.clock.tick(60)
        dt = self.clock.get_time()
        self.stage.update(dt)

    def render(self):
        self.display.fill(self.bg)
        self.stage.draw()
        self.stage.viewport.flip(self.display)
        pygame.display.flip()

    def change_stage(self, stage):
        self.stage = stage

game = RoboTrash()

while game.running:
    eventhandler.get()
    game.update()
    game.render()