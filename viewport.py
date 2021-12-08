import pygame

def Fit(surface, display):
    surfaceRect = surface.get_rect()
    displayRect = display.get_rect()

    fit = surfaceRect.fit(displayRect)
    scaled = pygame.transform.scale(surface, fit.size)
    display.blit(scaled, fit)

