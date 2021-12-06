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
        self.stack = []
        self.falling = []
        self.rotating = False
        self.npos = 0
        self.rect.x = type * 16

    def update(self, game):
        if self.npos != self.rect.x:
            diff = self.rect.x - self.npos
            direction = -1 if diff > 0 else 1
            self.rect.x += direction * 2

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(common.AnimatedSprite):
    spritesheet = pygame.image.load("assets/gameplay/player.tga")
    def __init__(self, botes):
        super().__init__(Player.spritesheet, (32, 16), 5, 0)
        self.back = True
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
        super().update(0.3)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move_left(self):
        if self.hand_left > 0:
            self.hand_right -= 1
            self.hand_left -= 1
            bote = self.botes[self.hand_left]
            self.rect.x = bote.npos
            self.row = 2 + self.back
            self.play()

    def move_right(self):
        if self.hand_right < len(self.botes) - 1:
            self.hand_left += 1
            self.hand_right += 1
            bote = self.botes[self.hand_left]
            self.rect.x = bote.npos
            self.row = 2 + self.back
            self.play()

    def rotate(self):
        self.back = not self.back
        self.row = 0 + self.back
        self.play()
        left = self.botes[self.hand_left]
        right = self.botes[self.hand_right]
        self.botes[self.hand_left] = right
        self.botes[self.hand_right] = left

class Gameplay:
    def __init__(self):
        self.surface = pygame.Surface((64, 128))
        self.pos = (16, 16)
        self.botes = [Bote(0), Bote(1), Bote(2), Bote(3)]
        self.player = Player(self.botes)

    def update(self, game):
        self.player.update(game)
        for i, bote in enumerate(self.botes):
            bote.npos = i * 16
            bote.update(game)

    def draw(self, surface):
        self.surface.fill(common.WHITE)
        for bote in self.botes:
            bote.draw(self.surface)
        self.player.draw(self.surface)
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

