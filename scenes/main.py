import pygame

class BlinkingText(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        font = pygame.font.Font("./assets/game_font.ttf", 8)
        self.image = font.render("Presiona Z para iniciar", False, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.opacity = 255
    def update(self):
        pass

class Stage:
    def __init__(self, game):
        self.eventManager = game.eventManager
        self.presiona_z = BlinkingText((game.size[0] / 2, game.size[1] / 2))
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.presiona_z)
    def update(self, dt):
        self.sprites.update()
    def draw(self, surface):
        self.sprites.draw(surface)
