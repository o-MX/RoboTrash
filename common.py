import pygame
from pygame import sprite
from pygame import font

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class SpriteSheet(pygame.sprite.Sprite):
    def __init__(self, image, tile):
        super().__init__()
        self.spritesheet = image
        self.spritepos = pygame.Rect((0, 0), tile)
        self.tile(0, 0)
        self.rect = self.image.get_rect()

    def tile(self, i, j):
        self.spritepos.x = int(j) * self.spritepos.width
        self.spritepos.y = int(i) * self.spritepos.height
        self.image = self.spritesheet.subsurface(self.spritepos)

class AnimatedSprite(SpriteSheet):
    def __init__(self, image, tile, frames, row):
        super().__init__(image, tile)
        self.tile(row, 0)
        self._frame = 0
        self._frames = frames
        self.looping = False
        self.animating = False
        self._row = 0

    def update(self, speed):
        if self.animating:
            self.tile(self._row, self._frame)
            self._frame += 1 * speed
            self.animating = self._frame <= self._frames or self.looping

    def play(self, row = 0, frame = 0):
        self._frame = frame
        self._row = row
        self.animating = True

class TextSprite(sprite.Sprite):
    def __init__(self, text, color, font_size):
        super().__init__()
        self.font = font.Font("assets/font2.ttf", font_size)
        self.image = self.font.render(text, False, color)
        self.rect = self.image.get_rect()
        self.color = color
        self.text = text

    def redraw(self):
        self.image = self.font.render(self.text, False, self.color)
        self.rect.size = self.image.get_size()

class Scene:
    def __init__(self, size, bg = None):
        self.pos = (0, 0)
        self.surface = pygame.Surface(size)
        self.group = sprite.Group()
        self.background = bg
        self.surface.blit(bg, self.pos)

    def update(self, game):
        self.group.update(game)

    def draw(self, surface: pygame.Surface):
        self.group.clear(self.surface, self.background)
        self.group.draw(self.surface)
        surface.blit(self.surface, self.pos)
