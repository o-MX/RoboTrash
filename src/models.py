from pygame import Rect, Surface
from pygame import transform, sprite

def _center_viewport(vpRect, sfRect):
    vpRect.x = (sfRect.width - vpRect.width) / 2
    vpRect.y = (sfRect.height - vpRect.height) / 2

class Viewport:
    def __init__(self, size, center):
        self.rect = Rect((0, 0), size)
        self.surface = Surface((self.rect.width,  self.rect.height))
        self.center = center
    def blit(self, surface):
        scaled = self.resize(surface.get_rect())
        if self.center:
            _center_viewport(self.rect, surface.get_rect())
        surface.blit(scaled, self.rect)
    def resize(self, dest):
        return transform.scale(self.surface, 
                (self.rect.width, self.rect.height))

class Stage:
    def __init__(self):
        self.bg = Stage.clear
        self.actors = sprite.Group()
    def act(self, surface, dt):
        self.actors.update(dt)
        self.actors.clear(surface, self.bg)
        self.actors.draw(surface)
    def clear(surface, rect):
        color = (0x00, 0x00, 0x00)
        surface.fill(color, rect)
