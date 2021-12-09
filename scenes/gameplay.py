import random, pygame, common
from pygame import mixer

class Scene(common.Scene):
    bg = pygame.image.load("assets/gameplay/gameplay.tga")
    cayendo_basura = mixer.Sound("assets/gameplay/cayendo.wav")

    def __init__(self):
        super().__init__((160, 160), Scene.bg)
        self.game_vp = pygame.Surface((16*4, 16*8))
        self.ticks = 0
        # Generar las columnas
        self.columnas = []
        for i in range(4):
            col = Column(i, i*16)
            self.columnas.append(col)
        # Poner a los sprites en pantalla
        self.score = Score(self.group)
        self.player = Player(0, 128)
        # Difficulty
        self.steps = 0
        self.prob = 2
        self.rate = 500
        # Play intro
        mixer.music.load("assets/gameplay/ingame.wav")
        mixer.music.play(-1)

    def update(self, game):
        super().update(game)
        self.ticks += game.clock.get_time()
        self.player.update(game)
        if self.ticks > self.rate:
            self.steps += 1
            self.steps %= 2
            for i in self.columnas:
                i.fall(self, 8)
                if len(i.stacked) > i.max:
                    game.change_scene("gameover")
            # Generate a random item
            if self.steps:
                # Scene.cayendo_basura.play()
                if random.randrange(0, self.prob) == 0:
                    sel = random.choice(self.columnas)
                    sel.random()
            self.ticks = 0

    def draw(self, surface):
        super().draw(surface)
        self.game_vp.fill(common.WHITE)
        for col in self.columnas:
            col.update()
            col.group.draw(self.game_vp)
        self.game_vp.blit(self.player.image, self.player.rect)
        surface.blit(self.game_vp, (16, 16))

class Column:
    basura_adentro = mixer.Sound("assets/gameplay/basura_dentro.wav")
    basura_erroneo = mixer.Sound("assets/gameplay/erroneo.wav")
    basura_borrada = mixer.Sound("assets/gameplay/basura_borrada.wav")
    cae_tapa = mixer.Sound("assets/gameplay/tapa.wav")
    tapa_cerrada = mixer.Sound("assets/gameplay/bote_cerrado.wav")

    def __init__(self, i, x):
        self.group = pygame.sprite.Group()
        self.stacked = [Bote(i, i * 16)]
        self.falling = []
        self.max = 7
        self.x = x
        self.group.add(self.stacked)
    
    def fall(self, scene, q):
        for i in self.falling:
            i.rect.y += q
        for i in self.falling.copy():
            top = self.stacked[-1]
            if i.rect.bottom > top.rect.y:
                if i.col != 3:
                    i.rect.bottom = top.rect.top
                    i.tile(i.type, i.col + 4)
                    self.stacked.append(i)
                    self.falling.remove(i)
                    if Basura.__instancecheck__(top):
                        if top.type == i.type and top.col == i.col:
                            self.stacked.remove(top)
                            self.stacked.remove(i)
                            self.group.remove(top, i)
                            scene.score.add_q(100)
                            Column.basura_borrada.play()
                else:
                    if Bote.__instancecheck__(top):
                        # Column.tapa_cerrada.play()
                        self.falling.remove(i)
                        self.group.remove(i)
                    else:
                        self.stacked.remove(top)
                        self.group.remove(top)
                        if self.stacked[0].type != 4:
                            if top.type == self.stacked[0].type:
                                Column.basura_adentro.play()
                                scene.score.add_q(100)
                            else:
                                Column.basura_erroneo.set_volume(0.2)
                                Column.basura_erroneo.play()
                                scene.score.add_q(-50)
                        else:
                            scene.score.add_q(-10)

    def random(self):
        type = random.randrange(0, 3)
        image = random.randrange(0, 4)
        basura = Basura(type, image, self.x)
        self.falling.append(basura)
        self.group.add(basura)

    def update(self):
        for i in self.group:
            diff = self.x - i.rect.x
            if diff != 0:
                i.rect.x += -2 if diff < 0 else 2

class Score(common.TextSprite):
    def __init__(self, group):
        super().__init__("0", common.WHITE, 8)
        self.add(group)
        self.rect.x = 16*6 + 2
        self.rect.y = 20
        self.score = 0
    def add_q(self, q):
        self.score += q
        self.text = str(self.score)
        self.redraw()
        return self.score

class Player(common.AnimatedSprite):
    girar_sound = mixer.Sound("assets/gameplay/giro.wav")
    mover_sound = mixer.Sound("assets/gameplay/move.wav")
    sprite = pygame.image.load("assets/gameplay/player.tga")

    def __init__(self, x, y):
        super().__init__(Player.sprite, (32, 16), 4, 0)
        self.rect.x = x
        self.rect.bottom = y
        self.rotated = False
        self.pos = 0

    def update(self, game):
        super().update(0.4)
        if game.events.isKeyDown(pygame.K_z):
            self.rotate(game.scene.columnas)
        if game.events.isKeyDown(pygame.K_LEFT):
            self.move(-1, game.scene.columnas) 
        elif game.events.isKeyDown(pygame.K_RIGHT):
            self.move(1, game.scene.columnas)

    def move(self, direction, list):
        Player.mover_sound.set_volume(0.2)
        Player.mover_sound.play()
        npos = self.pos + direction
        if npos >= 0 and npos < len(list) - 1:
            self.pos = npos
        self.rect.x = list[self.pos].x
        self.play(2 + self.rotated)
    
    def rotate(self, list):
        Player.girar_sound.set_volume(0.2)
        Player.girar_sound.play()
        self.play(self.rotated)
        self.rotated = not self.rotated
        # Swap falling
        left = list[self.pos]
        right = list[self.pos+1]
        aux = left.falling
        left.group.remove(left.falling) 
        left.falling = right.falling
        left.group.add(left.falling) 
        right.group.remove(right.falling) 
        right.falling = aux
        right.group.add(right.falling) 
        for i in left.falling.copy():
            if i.rect.bottom > left.stacked[-1].rect.y:
                left.falling.remove(i)
                left.group.remove(i)
                right.falling.append(i)
                right.group.add(i)
        for i in right.falling.copy():
            if i.rect.bottom > right.stacked[-1].rect.y:
                right.falling.remove(i)
                right.group.remove(i)
                left.falling.append(i)
                left.group.add(i)

        # Swap botes
        list[self.pos] = right
        list[self.pos+1]= left
        aux = left.x
        left.x = right.x
        right.x = aux
        for i in right.falling:
            i.rect.x = right.x
        for i in left.falling:
            i.rect.x = left.x

class Bote(common.SpriteSheet):
    sprite = pygame.image.load("assets/gameplay/trashcans.tga")

    def __init__(self, type, pos):
        super().__init__(Bote.sprite, (16, 16))
        self.type = type
        self.rect.x = pos
        self.rect.bottom = 128
        self.tile(0, type)

class Basura(common.SpriteSheet):
    sprite = pygame.image.load("assets/gameplay/trash.tga")
    def __init__(self, type, img, x):
        super().__init__(Basura.sprite, (16, 16))
        self.type = type
        self.col = img  
        self.tile(type, img)
        self.rect.x = x
        self.rect.y = 0
