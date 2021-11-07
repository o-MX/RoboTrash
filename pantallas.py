import pygame, sys
import utils

class Inicio:
    def __init__(self, game):
        pygame.mixer.music.load('Assets/std_song.wav')
        pygame.mixer.music.play(3)
        self.game = game
        self.bg = pygame.image.load("./Assets/main_bg.png")
        self.title = pygame.image.load("./Assets/title.png")
        self.personje = pygame.image.load("./Assets/cabeza.png") 
        self.personje = pygame.transform.scale(self.personje, (35,28)) 
        utils.TextoAnimado.__init__(self) #TRAIGO DE UTILS.PY EL TEXTO CON SUS PROPIEDADES
        
    def draw(self, vp):
        vp.blit(self.bg, (0, 0))
        vp.blit(self.title, (20, 20))
        vp.blit(self.personje, (70,120))
        utils.TextoAnimado.render(self,vp) #TRAIGO DE UTILS LA POSICION DEL TEXTO


    def update(self, dt):
        if(utils.Events.isKeyDown(pygame.K_RETURN)):
            self.game.changeStage(Inicio(self.game))
        utils.TextoAnimado.update(self,dt)

