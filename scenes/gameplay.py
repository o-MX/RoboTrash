import pygame
import common

class Score(common.TextSprite):
    def __init__(self, group):
        super().__init__("0", common.WHITE, 8)
        self.rect.x = 100
        self.rect.y = 20
        self.score = 0
        group.add(self)

    def add_score(self, score):
        self.score += score
        self.text = str(self.score)
        self.redraw()

class Bote(common.SpriteSheet):
    spritesheet = pygame.image.load("assets/gameplay/trashcans.tga")
    def __init__(self, type):
        super().__init__(Bote.spritesheet, (16, 16))
        self.tile(type, 0)
        self.type = type
        self.rect.bottom = 128

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(common.AnimatedSprite):
    spritesheet = pygame.image.load("assets/gameplay/player.tga")
    def __init__(self, botes):
        super().__init__(Player.spritesheet, (32, 16), 5, 0)
        self.facing_front = True
        self.animation_speed = 0.4
        self.rect.bottom = 128
        self.hand_left = 0
        self.hand_right = 1
        self.botes = botes

    def update(self, game):
        if game.events.isKeyDown(pygame.K_z):
            self.rotate()
        if game.events.isKeyDown(pygame.K_LEFT):
            self.move_left()
        elif game.events.isKeyDown(pygame.K_RIGHT):
            self.move_right()
        super().update(self.animation_speed)

    def move_left(self):
        if self.hand_left > 0:
            self.hand_right = self.hand_left
            self.hand_left -= 1
            bote = self.botes[self.hand_left]
            self.rect.x = bote.rect.x

    def move_right(self):
        if self.hand_right < len(self.botes) - 1:
            self.hand_left = self.hand_right
            self.hand_right += 1
            bote = self.botes[self.hand_left]
            self.rect.x = bote.rect.x

    def rotate(self):
        self.row = 0
        self.play()
        self.animation_speed *= -1

class Gameplay:
    def __init__(self):
        self.surface = pygame.Surface((64, 128))
        self.pos = (16, 16)
        self.botes = [Bote(0), Bote(1), Bote(2), Bote(3)]
        self.player = Player(self.botes)

    def update(self, game):
        self.player.update(game)

    def draw(self, surface):
        self.surface.fill(common.WHITE)
        for i, bote in enumerate(self.botes):
            bote.rect.x = i * 16
            bote.draw(self.surface)
        self.surface.blit(self.player.image, self.player.rect)
        surface.blit(self.surface, self.pos)

class Scene(common.Scene):
    bg = pygame.image.load("assets/gameplay/gameplay.tga")
    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        self.score = Score(self.group)
        self.gameplay = Gameplay()

    def update(self, game):
        super().update(game)
        self.gameplay.update(game)

    def draw(self, surface):
        super().draw(surface)
        self.gameplay.draw(self.surface)

