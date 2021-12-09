import pygame
from pygame.mixer import music
import common
import easing

class Title(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("assets/main/title.tga")
        self.rect = self.image.get_rect()
        self.centerx = 80
        self.bouncing = easing.Ease(1000, easing.inOutBack, 10)

    def update(self, game):
        super().update()
        self.bouncing.update(game.clock.get_time())
        self.rect.y = self.bouncing.val

class Label(common.TextSprite):
    def __init__(self, group):
        super().__init__("Presiona Z para iniciar",
                         common.BLACK, 8)
        self.rect.center = (80, 110)
        self.blink = easing.Ease(623, easing.sinEaseIn, 255, True)
        group.add(self)

    def update(self, game):
        self.blink.update(game.clock.get_time())
        self.image.set_alpha(self.blink.val)

class Scene(common.Scene):
    bg = pygame.image.load("assets/main/bg.tga")
    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        # Play game main music
        music.load("assets/main/music.wav")
        music.play(-1)
        # Add sprites to group
        Title(self.group)
        Label(self.group)

    def update(self, game):
        super().update(game)
        if game.events.isKeyDown(pygame.K_z):
            music.stop()
            game.change_scene("story")

    def draw(self, surface):
        super().draw(surface)
