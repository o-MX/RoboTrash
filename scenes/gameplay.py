import pygame, random

class Basura(pygame.sprite.Sprite):
    ORGANICA = 0
    INORGANICA = 1
    BIOLOGICA = 2
    GENERICA = 3
    atlas = pygame.image.load("assets/trash.tga")
    def __init__(self, _type: int, i: int):
        super().__init__()
        self.falling = True
        self.image = Basura.atlas.subsurface(i * 16, 16 * _type, 16, 16)
        self.rect = self.image.get_rect()
    def update(self, dt, eventManager):
        pass

class Bote(pygame.sprite.Sprite):
    atlas = pygame.image.load("assets/trashcans.tga")
    def __init__(self, pos, _type: int):
        super().__init__()
        global BOTES
        self.type = _type
        self.image = Bote.atlas.subsurface((16 * _type, 0), (16, 8))
        self.rect = self.image.get_rect()
        self.rect.x = pos * 20 + 2
        self.rect.bottom = 144 - 6
        self.stack = []

class Player(pygame.sprite.Sprite):
    def __init__(self, botes):
        super().__init__()
        self.sprites = [
            pygame.image.load("assets/player_back.tga"),
            pygame.image.load("assets/player_front.tga")
        ]
        self.rotation = 0
        self.current = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = 144
        self.botes = botes
        self.rect.centerx = self.botes[self.current].rect.right + 2
    def update(self, dt, eventManager):
        if eventManager.isKeyDown(pygame.K_z):
            self.rotate()
        if eventManager.isKeyDown(pygame.K_LEFT):
            self.move(-1)
        elif eventManager.isKeyDown(pygame.K_RIGHT):
            self.move(1)
    def rotate(self):
        self.rotation += 1
        self.rotation %= 2
        self.image = self.sprites[self.rotation]
        # Mover botes
        current = self.botes[self.current]
        _next = self.botes[self.current + 1]
        aux = current.rect.copy()
        current.rect = _next.rect.copy()
        _next.rect = aux
        for t in current.stack:
            if t.falling:
                for t2 in _next.stack:
                    t.rect.x += 16
                    if not t.rect.colliderect(t2.rect):
                        _next.stack.append(t)
                        current.stack.remove(t)
                    else:
                        t.rect.x -= 16
        self.botes[self.current] = _next
        self.botes[self.current + 1] = current
    def move(self, quant):
        new_pos = self.current + quant
        if new_pos >= 0 and new_pos < len(self.botes) - 1:
            self.current = new_pos
            self.rect.centerx = self.botes[self.current].rect.right + 2

class Stage:
    def __init__(self, game):
        self.eventManager = game.eventManager
        self.sprites = pygame.sprite.Group()
        self.ui = pygame.sprite.Group()
        self.bg = pygame.image.load("assets/gameplay.tga")
        self.game = pygame.Surface((80, 144))
        self.botes = [
            Bote(0, Basura.ORGANICA),
            Bote(1, Basura.INORGANICA),
            Bote(2, Basura.BIOLOGICA),
            Bote(3, Basura.GENERICA)
        ]
        self.player = Player(self.botes)
        self.clock = pygame.time.Clock()
        self.time = 0
    def update(self, dt):
        self.sprites.update(dt, self.eventManager)
        self.time += dt
        if self.time > 3000:
            for b in self.botes:
                basura = random.randint(0, 1)
                random.seed(random.random())
                if basura:
                    sprite = random.randint(0, 2)
                    random.seed(random.random())
                    _type = random.randint(0, 2)
                    random.seed(random.random())
                    residuo = Basura(_type, sprite)
                    b.stack.append(residuo)
                    residuo.rect.x = b.rect.x
                    self.sprites.add(residuo)
            self.time = 0
    def draw(self, surface):
        surface.blit(self.bg, (0, 0))

        # Render game
        self.game.fill((255, 255, 255))
        self.sprites.draw(self.game)
        surface.blit(self.game, (32, 16))
    def start(self):
        self.sprites.add(self.botes)
        self.sprites.add(self.player)
