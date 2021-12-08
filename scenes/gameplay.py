import random, pygame, common

class Scene(common.Scene):
    bg = pygame.image.load("assets/gameplay/gameplay.tga")
    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        self.score = Score()
        self.game = Game(self.score)
        self.columns = []
    def update(self, game):
        super().update(game)
        self.game.update(game)
    def draw(self, surface):
        super().draw(surface)
        self.game.draw(surface)

class Score(common.TextSprite):
    def __init__(self):
        super().__init__("0", common.WHITE, 8)
        self.score = 0
        self.rect.x = 16*6 + 2
        self.rect.y = 20
    def add(self, q):
        self.score += q
        self.text = str(self.score)
        self.redraw()

class Column:
    def __init__(self, bote):
        self.rect = pygame.Rect(bote.type * 16, 0, 16, 16*8)
        self._items = [bote]
        self.stacked = [bote]
        self.falling = []
        self.max = 5
    def draw(self, surface):
        for i in self._items:
            surface.blit(i.image, i.rect)
    def update(self):
        for item in self.stacked:
            item.move(self.rect.x)
    def push_down(self, score):
        top = self.stacked[-1]
        for i in self.falling:
            i.fall()
            if i.rect.bottom >= top.rect.top:
                i.rect.bottom = top.rect.top
                self.stacked.append(i)
                self.falling.remove(i)
                i.tile(i.type, i.col + 4)
                if Basura.__instancecheck__(top):
                    if i.type == top.type and i.col == top.col:
                        self.stacked.remove(i)
                        self._items.remove(i)
                        self.stacked.remove(top)
                        self._items.remove(top)
                        score.add(100)
    def random(self):
        type = random.randrange(0, 3)
        col = random.randrange(0, 3)
        basura = Basura(type, col, self.rect.x)
        self._items.append(basura)
        self.falling.append(basura)

class Game:
    def __init__(self, score):
        self.surface = pygame.Surface((16*4, 16*8))
        self.columnas = []
        self.score = score
        for i in range(4):
            col = Column(Bote(i))
            self.columnas.append(col)
        self.time = 0
        self.player = Player(self.columnas)
    def update(self, game):
        if game.events.isKeyDown(pygame.K_z):
            self.player.rotate()
        if game.events.isKeyDown(pygame.K_LEFT):
            self.player.move(-1)
        elif game.events.isKeyDown(pygame.K_RIGHT):
            self.player.move(1)
        # Game clock
        self.time += game.clock.get_time()
        if self.time > 1000:
            for col in self.columnas:
                col.push_down(self.score)
            # Generate a random trash
            if random.randint(0, 3) == 0:
                sel = random.randrange(0, len(self.columnas))
                self.columnas[sel].random()
            self.time = 0
        self.player.update(game)
        for i, col in enumerate(self.columnas):
            col.rect.x = 16*i
            col.update()
    def draw(self, surface):
        self.surface.fill(common.WHITE)
        # Draw the game columns
        for col in self.columnas:
            col.draw(self.surface)
        # Draw the player
        self.surface.blit(self.player.image, self.player.rect)
        surface.blit(self.score.image, self.score.rect)
        surface.blit(self.surface, (16, 16))

class Player(common.AnimatedSprite):
    sprite = pygame.image.load("assets/gameplay/player.tga")
    def __init__(self, columnas):
        super().__init__(Player.sprite, (32, 16), 5, 0)
        self.rect.x = 0
        self.rect.bottom = 128
        self.columnas = columnas 
        self.current = 0
        self.rotated = False
        self.lhand = self.columnas[0]
        self.rhand = self.columnas[1]
    def update(self, game):
        super().update(0.4)
    def move(self, direction):
        npos = self.current + direction
        max = len(self.columnas) - 1
        if npos > -1 and npos < max:
            self.current = npos
            self.rect.x = self.current * 16
            self.lhand = self.columnas[self.current]
            self.rhand = self.columnas[self.current + 1]
        self.row = 2 + self.rotated
        self.play()
    def rotate(self):
        # Change falling
        aux = []
        for i in self.lhand.falling:
            collided = False
            i.rect.x = self.rhand.rect.x
            for j in self.rhand._items:
                if i.rect.colliderect(j):
                    collided = True
                    break
            if not collided:
                i.rect.x = self.lhand.rect.x
                aux.append(i)
                self.lhand._items.remove(i)
                self.lhand.falling.remove(i)
        for i in self.rhand.falling:
            collided = False
            i.rect.x = self.lhand.rect.x
            for j in self.lhand._items:
                if i.rect.colliderect(j):
                    collided = True
                    break
            if not collided:
                i.rect.x = self.rhand.rect.x
                self.lhand._items.append(i)
                self.lhand.falling.append(i)
                self.rhand._items.remove(i)
                self.rhand.falling.remove(i)
        for i in aux:
            self.rhand._items.append(i)
            self.rhand.falling.append(i)
        self.columnas[self.current] = self.rhand
        self.columnas[self.current+1] = self.lhand
        self.lhand =self.columnas[self.current]
        self.rhand = self.columnas[self.current+1]
        # Play animation
        self.row = 0 + self.rotated
        self.rotated = not self.rotated
        self.play()

class Bote(common.SpriteSheet):
    sprite = pygame.image.load("assets/gameplay/trashcans.tga")
    def __init__(self, type):
        super().__init__(Bote.sprite, (16, 16))
        self.tile(0, type)
        self.rect.bottom = 16*8
        self.rect.x = type * 16
        self.type = type
    def move(self, npos):
        diff = self.rect.x - npos
        if diff != 0:
            self.rect.x += -2 if diff > 0 else 2

class Basura(common.SpriteSheet):
    sprite = pygame.image.load("assets/gameplay/trash.tga")
    def __init__(self, type, basura, x):
        super().__init__(Basura.sprite, (16, 16))
        self.tile(type, basura)
        self.rect.x = x
        self.rect.y = 0
        self.type = type
        self.col = basura
    def fall(self):
        self.rect.y += 16
    def move(self, npos):
        diff = self.rect.x - npos
        if diff != 0:
            self.rect.x += -2 if diff > 0 else 2
