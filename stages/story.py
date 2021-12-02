import assets, pygame, math, sys, src
from src import eventhandler
from pygame import Rect, Surface
from pygame.sprite import Sprite
from pygame import transform
from pygame.mixer import music
from src.models import Stage

class Screen(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = transform.chop(assets.bg_main, (0, 0, 20, 110))
        self.rect = self.image.get_rect()
        self.rect.centerx = src.CENTER_SCREEN[0]
        self.rect.y += 10

class HistoryText(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = Surface((src.SCREEN_SIZE[0], src.CENTER_SCREEN[1]))
        self.rect = self.image.get_rect()
        self.rect.y = src.CENTER_SCREEN[1]
        self.line = 0
        self.line_width = 28
        self.time = 0
        self.next_paragraph()
    def next_paragraph(self):
        pass
    def update(self, dt):
        pass

class Story(Stage):
    vista = False
    def __init__(self, surface):
        Stage.__init__(self)
        surface.fill(src.BLACK)
        self.actors.add(Screen())
        self.actors.add(HistoryText())
        if Story.vista:
            pass
    def act(self, surface, dt):
        Stage.act(self, surface, dt)
