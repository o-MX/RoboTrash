from pygame import Rect
from pygame.sprite import Sprite
from pygame import transform
from src.models import Stage
import assets

class Title(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.title
        self.rect = self.image.get_rect()
        self.rect.x = (192 - self.rect.width)/2
        self.rect.y = (176 - self.rect.height)/2
        self.rect.y -= 35

class Head(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = assets.head
        self.time = 0

        self.rect = self.image.get_rect()
        self.rect.x = (192 - self.rect.width)/2
        self.rect.y = 176 - self.rect.height
        self.rect.y -= 25

class Menu(Stage):
    def __init__(self):
        Stage.__init__(self)
        self.bg = assets.bg_main
        self.actors.add(Title())
        self.actors.add(Head())
    def act(self, surface, dt):
        surface.blit(self.bg, self.bg.get_rect())
        Stage.act(self, surface, dt)
