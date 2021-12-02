import pygame

def Fit(surface: pygame.Surface, display: pygame.Surface):
    surfaceRect = surface.get_rect()
    displayRect = display.get_rect()

    fit = surfaceRect.fit(displayRect)
    scaled = pygame.transform.scale(surface, fit.size)
    display.blit(scaled, fit)

