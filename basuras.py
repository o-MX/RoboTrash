import pygame, sys


class Basura_principal:
	def __init__(self):
            self.fall_sprite = None
            self.idle_sprite = None
            self.velocidad = 0
            self.posicion_x = 0
            self.posicion_y = 0
            self.estado = 'callendo'

class Inorganica(Basura_principal):
	def __init__(self):
            Basura_principal.__init__(self)
            self.sprite = None

class Organica(Basura_principal):
	def __init__(self):
            Basura_principal.__init__(self)
            self.sprite = None

class Sanitaria(Basura_principal):
	def __init__(self):
            Basura_principal.__init__(self)
            self.sprite = None
