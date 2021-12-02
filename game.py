import pygame
import viewport
import scenes
pygame.init()

class EventManager:
    def __init__(self):
        self._keysDown= []
        self.onQuit = []
        self.onChangeScene = []
    def handle(self):
        self._keysDown.clear()
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                self._keysDown.append(e)
            elif e.type == pygame.QUIT:
                for evL in self.onQuit:
                    evL()
    def quit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    def change_scene(self, scene_id):
        for evL in self.onChangeScene:
            evL(scene_id)

class Game:
    def __init__(self):
        self.size = (192, 176)
        self.fps = 60
        self.bgColor = 0, 0, 0
        self.clock = pygame.time.Clock()
        self.running = True
        self.surface = pygame.Surface(self.size)
        self.eventManager = EventManager()
        self.eventManager.onQuit.append(self.quit_game)
        self.eventManager.onChangeScene.append(self.change_scene)
        self.scene = scenes.get("main", self)
    def update(self):
        self.clock.tick(self.fps)
        self.eventManager.handle()
        self.scene.update(self.clock.get_time())
    def draw(self):
        self.scene.draw(self.surface)
    def quit_game(self):
        self.running = False
    def change_scene(self, id):
        self.scene = scenes.get(id, self)

display = pygame.display.set_mode((700, 600), pygame.RESIZABLE)
game = Game()
while game.running:
    game.update()
    game.draw()
    viewport.Fit(game.surface, display)
    pygame.display.flip()

pygame.quit()
exit()
