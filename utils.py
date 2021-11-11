import pygame, sys
import assets

class HealthIndicator:
    def __init__(self):
        self.lives = 3
        self.health = self.lives
        self.__padding = 2
        self.size = (12, 11)
        self.surface = pygame.Surface(
            (self.size[0] * self.lives + self.__padding  * (self.lives - 1), self.size[1]), 
            pygame.SRCALPHA, 32)
        self.render_health()

    def take_damage(self, quant):
        self.health -= quant
        self.render_health()

    def render_health(self):
        rest = self.health
        for i in range(self.lives):
            hrt_rect = pygame.Rect((0, 0), self.size)
            if rest <= 0:
                hrt_rect.x = self.size[0] * 2
            elif rest < 1:
                hrt_rect.x = self.size[0]
            subsrf = assets.hearts_sprite.subsurface(hrt_rect)
            self.surface.blit(subsrf, (i * self.size[0] + i * self.__padding, 0))
            rest -= 1

class TextoAnimado:
    def __init__(self, texto, tiempo):
        self.opacidad = 0
        self.milisegundos = 0
        self.tiempo = tiempo
        self.aumento = 10
        self.font = pygame.font.Font("./Assets/dogicapixel.ttf", 8)
        self.text = self.font.render(texto, 0, (0, 0, 0))
        self.pos = (0, 0)

    def render(self, vp):
        vp.blit(self.text, (self.pos))

    def update(self, dt):
        self.text.set_alpha(self.opacidad)
        self.milisegundos += dt
        self.opacidad += self.aumento
        if self.milisegundos > self.tiempo:
            self.milisegundos = 0
            self.aumento = -self.aumento

class MoveImg:
    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0
        self.moveimg = .2
        self.img = assets.head_sprite

    def render(self,vp):
        vp.blit(self.img, (self.coord_x, self.coord_y))

    def update(self):
        if self.coord_x > 80 or self.coord_x < 70:
            self.moveimg = self.moveimg * -1
        self.coord_x += self.moveimg

