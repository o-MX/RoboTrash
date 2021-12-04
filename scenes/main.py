import pygame
from pygame.mixer import music
import common
import easing

class Title(common.AnimatedSprite):
    def __init__(self):
        super().__init__("main/title", 3, 0.15)
        self.time = 0
        self.centerx = 80

    def update(self, game):
        super().update(game)

    def bounce(self, ease, f):
        self.rect.y = f * 10

class Label(common.TextSprite):
    def __init__(self):
        super().__init__("Presiona Z para iniciar", common.BLACK, 12)
        self.font = pygame.font.Font("assets/font2.ttf", 8)
        self.redraw()
        self.rect.center = (80, 110)
        # self.ease = easing.Ease(623, easing.sinEaseIn, self.blink, -1)

    def update(self, stage):
        # self.ease.update()
        pass

    def blink(self, ease, f):
        self.image.set_alpha(255 * f)

class Scene(common.Scene):
    bg = (0xb9, 0xe5, 0xe5)
    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        self.title = Title()
        self.label = Label()

        music.load("assets/main/music.wav")
        music.play()

        # Add sprites to group
        self.group.add(self.title)
        self.group.add(self.label)

    def update(self, game):
        super().update(game)
        if game.events.isKeyDown(pygame.K_z):
            music.fadeout(500)

    def draw(self, surface):
        super().draw(surface)
