import pygame
from pygame import sprite
from pygame import image
from pygame import font

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class SpriteAtlas(sprite.Sprite):
    def __init__(self,
                 atlas: pygame.Surface,
                 tile_size: tuple[float, float]):
        super().__init__()
        self.atlas = atlas
        self.tile = tile_size

    def get_tile(self, i, j):
        pos = self.tile[0] * i, self.tile[1] * j
        sprite = self.atlas.subsurface(pos, self.tile)
        return sprite

class AnimatedSprite(sprite.Sprite):
    def __init__(self,
                 name: str,
                 frames: int,
                 speed: float):
        super().__init__()
        self.animating = True
        self.frame = 0
        self.frames = []
        self.frame_speed = speed
        self.current_frame = 0
        for i in range(frames):
            file = image.load("assets/" + name + str(i) + ".tga")
            self.frames.append(file)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()

    def update(self, game):
        if self.animating:
            self.current_frame += self.frame_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            frame = int(self.current_frame)
            self.image = self.frames[frame]

    def reset_animation(self, frame = 0):
        self.image = self.frames[frame]
        self.animating = True

class TextSprite(sprite.Sprite):
    def __init__(self, text, color, font_size):
        super().__init__()
        self.font = pygame.font.Font("assets/font.ttf", font_size)
        self.color = color
        self.text = text
        self.image = self.font.render(text, False, color)
        self.rect = self.image.get_rect()

    def redraw(self):
        self.image = self.font.render(self.text, False, self.color)
        self.rect = self.image.get_rect()

class Scene:
    def __init__(self, size, bg_color):
        self.pos = (0, 0)
        self.surface = pygame.Surface(size)
        self.group = sprite.Group()
        self.surface.fill(bg_color)
        self.bg = self.surface.copy()
        self.queue = []

    def update(self, game):
        self.group.update(self)
        for e in self.queue:
            e.update()

    def draw(self, surface: pygame.Surface):
        self.group.clear(self.surface, self.bg)
        self.group.draw(self.surface)
        surface.blit(self.surface, self.pos)
