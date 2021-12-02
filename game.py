import pygame, sys
import viewports
import stages
import constants as c

SCREEN = pygame.display.set_mode(c.SCREEN_SIZE, c.FLAGS)

def main():
    running = True
    clock = pygame.time.Clock()
    viewport = viewports.Fit(c.SIZE)
    stage = None

    while running:
        running = not pygame.event.peek(pygame.QUIT)
        change_req = pygame.event.get(c.CHANGE_SCREEN)
        if change_req:
            stage = change_req.stage
        viewport.display(SCREEN)
        pygame.display.flip()

if __name__ == '__main__':
    main()
