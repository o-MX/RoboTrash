from pygame.transform import scale
from src.models import Viewport

class Fit(Viewport):
    def __init__(self, size, center):
        Viewport.__init__(self, size, center)
    def resize(self, dest):
        self.rect = self.rect.fit(dest)
        return scale(self.surface, (self.rect.width, self.rect.height))

