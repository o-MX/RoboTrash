import pygame, sys
import events, viewports, assets
import constants as c
pygame.init()
assets.load()

class MainScene():
    def __init__(self, game):
        self.sprites = pygame.sprite.Group()
        self.bg = assets.bg_main
        self.game = game
        self.title_rect = assets.title.get_rect()
        self.title_rect.centerx = game.size[0] / 2
        self.title_rect.y = 10
    def act(self, dt):
        pass
    def draw(self, surface):
        surface.blit(assets.title, self.title_rect)
        pass

class Game:
    def __init__(self, size):
        self.size = size
        self._display = pygame.display.set_mode(
            (700, 600), pygame.RESIZABLE)
        self.running = True
        self._clock = pygame.time.Clock()
        self._viewport = viewports.Fit(size)
        self._fps = 60
        self._scene = MainScene(self)
    def update(self):
        self._clock.tick(self._fps)
        self.running = not pygame.event.peek(pygame.QUIT)
        self._viewport.display(self._display)
        self._scene.act(self._clock.get_time())
        self._scene.draw(self._viewport.surface)
    def change_scene(scene):
        self.scene = scene

def main():
    game = Game((176, 192))
    while game.running:
        events.handle()
        game.update()
        pygame.display.flip()

if __name__ == '__main__':
    main()
