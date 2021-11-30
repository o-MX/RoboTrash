from pygame import Rect, Surface
from pygame import transform, sprite

class Viewport:
    def __init__(self, size, center):
        self.rect = Rect((0, 0), size)
        self.surface = Surface((self.rect.width,  self.rect.height))
    def blit(self, surface):
        scaled = self.resize(surface.get_rect())
        surface.blit(scaled, self.rect)
    def resize(self, dest):
        return transform.scale(self.surface,
                (self.rect.width, self.rect.height))

class Stage:
    def __init__(self):
        self.bg = lambda s, r: s.fill((0, 0, 0), r)
        self.actors = sprite.Group()
    def act(self, surface, dt):
        self.actors.update(dt)
        self.actors.clear(surface, self.bg)
        self.actors.draw(surface)
    def set_display(self, surface):
        surface.blit(self.bg, (0, 0))
