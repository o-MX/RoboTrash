# Proyecto ṔI 1 UCOL
import sys, pygame
pygame.init()

size = width, height = 16*12, 16*11
black = 0, 0, 0
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    screen.fill(black)
    pygame.display.flip()
