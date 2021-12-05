import pygame
pygame.init()
import viewport
import scenes

class EventManager:
    def __init__(self):
        self._keysDown= []
        self.quit = False

    def handle(self):
        self._keysDown.clear()
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                self._keysDown.append(e)
            elif e.type == pygame.QUIT:
                self.quit = True

    def isKeyDown(self, key_code):
        for k in self._keysDown:
            if k.key == key_code:
                return True
        return False

class Game:
    def __init__(self):
        self.size = (160, 160)
        self.fps = 60
        self.bgColor = 0, 0, 0
        self.clock = pygame.time.Clock()
        self.running = True
        self.surface = pygame.Surface(self.size)
        self.events = EventManager()
        self.change_scene("main")

    def update(self):
        self.clock.tick(self.fps)
        self.running = not self.events.quit
        self.events.handle()
        self.scene.update(self)

    def draw(self, display):
        self.surface.fill((0, 0, 0))
        self.scene.draw(self.surface)
        viewport.Fit(game.surface, display)

    def change_scene(self, scene_id):
        self.scene = scenes.get(scene_id)

SCREEN_SIZE = (700, 600)
display = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
game = Game()
while game.running:
    game.update()
    game.draw(display)
    pygame.display.flip()

pygame.quit()
exit()
