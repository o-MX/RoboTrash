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
        self.spritepos.x = int(i) * self.spritepos.width
        self.spritepos.y = int(j) * self.spritepos.height
        self.image = self.spritesheet.subsurface(self.spritepos)

class AnimatedSprite(SpriteSheet):
    def __init__(self, image, tile, frames, row):
        super().__init__(image, tile)
        self.tile(0, row)
        self.frame = 0
        self.row = row
        self.frames = frames
        self.looping = False
        self.animating = False

    def update(self, speed):
        if self.animating:
            self.frame += 1 * speed
            if self.frame > self.frames or self.frame < 0:
                self.animating = False or self.looping
            else:
                self.tile(self.frame, self.row)

    def restart(self):
        self.frame = 0

    def play(self):
        self.animating = True

    def loop(self, looping):
        self.looping = looping

class TextSprite(sprite.Sprite):
    def __init__(self, text, color, font_size):
        super().__init__()
        self.font = font.Font("assets/font2.ttf", font_size)
        self.color = color
        self.text = text
        self.image = self.font.render(text, False, color)
        self.rect = self.image.get_rect()

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
