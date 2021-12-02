import pygame
import utils

class BlinkingText(utils.Texto):
    def __init__(self):
        super().__init__(size = 12,
            text = "Presiona Z para iniciar",
            color = (255, 255, 255))
        self.rect = self.image.get_rect()
        self.time = 0
    def update(self, dt):
        self.time += dt
        self.time %= 1000
        t = self.time / 1000
        opacity = 4 * t * (1 - t)
        self.image.set_alpha(opacity * 255)

class Stage:
    def __init__(self, game):
        self.eventManager = game.eventManager
        self.presiona_z = BlinkingText()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.presiona_z)
        self.bg = pygame.image.load("assets/main.tga")
        pygame.mixer.music.load("assets/main_song.wav")
        pygame.mixer.music.play(-1)
    def update(self, dt):
        if self.eventManager.isKeyDown(pygame.K_z):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self.eventManager.change_scene("story")
        self.sprites.update(dt)
    def draw(self, surface):
        surface.blit(self.bg, (0, 0))
        self.sprites.draw(surface)
    def start(self):
        self.presiona_z.rect.center = (192 / 2, 176 / 2 + 10)
