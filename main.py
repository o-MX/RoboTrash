import sys, pygame
from pygame.time import Clock
import assets
from src import eventhandler
from src import viewports
from src.stages.menu import Menu
pygame.init()
assets.load()
eventhandler.init()

class RoboTrash:
    def __init__(self):
        self.size = (700, 600)
        self.bg = (0, 0, 0)
        self.running = True
        self.clock = Clock()
        # Creating the display
        flags = pygame.RESIZABLE
        self.display = pygame.display.set_mode(self.size, flags)
        self.viewport = viewports.Fit((192, 176), True)
        self.stage = Menu()
    def update(self):
        self.clock.tick(60)
        dt = self.clock.get_time()
        eventhandler.get()
        self.running = not eventhandler.quit
        self.stage.act(self.viewport.surface, dt)
    def render(self):
        self.display.fill((0, 0, 0))
        self.viewport.blit(self.display)
        pygame.display.flip()

game = RoboTrash()

while game.running:
    game.update()
    game.render()
