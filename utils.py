import pygame

class Texto(pygame.sprite.Sprite):
    def __init__(self, text, size, font = "game_font.ttf", color = (0, 0, 0)):
        super().__init__()
        self.size = size
        self.text = text
        self.color = color
        self.font = font
        self.render()
        self.rect = self.image.get_rect()
    def render(self):
        self._font = pygame.font.Font("assets/" + self.font, self.size)
        self.image = self._font.render(self.text, False, self.color)
