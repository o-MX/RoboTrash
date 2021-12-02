import pygame

class BlinkingText(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        font = pygame.font.Font("./assets/game_font.ttf", 12)
        self.image = font.render("Presiona Z para iniciar", False, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = center
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
        self.presiona_z = BlinkingText(
            (game.size[0] / 2, game.size[1] / 2 + 12)
        )
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.presiona_z)
        self.bg = pygame.image.load("./assets/bg0.tga")
        pygame.mixer.music.load("./assets/main_song.wav")
        pygame.mixer.music.play()
    def update(self, dt):
        if self.eventManager.isKeyDown(pygame.K_z):
            self.eventManager.change_scene("story")
            pygame.mixer.music.stop()
        self.sprites.update(dt)
    def draw(self, surface):
        surface.blit(self.bg, (0, 0))
        self.sprites.draw(surface)
