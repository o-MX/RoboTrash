from pygame import transform, Rect, Surface

class _Viewport:
    def __init__(self, size):
        self.rect = Rect((0, 0), size)
        self.surface = Surface(size)
    def display(self, surface):
        scaled = self.resize(surface.get_rect())
        surface.blit(scaled, self.rect)
    def resize(self, dest):
        return transform.scale(self.surface, dest.size)

class Fit(_Viewport):
    def __init__(self, size):
        _Viewport.__init__(self, size)
    def resize(self, dest):
        self.rect = self.rect.fit(dest)
        return transform.scale(self.surface, self.rect.size)
