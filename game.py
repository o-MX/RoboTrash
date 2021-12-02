from pygame import *
from utils import *
from stages import menu, story, gameover
import events
import assets
import viewports
init()
events.init()
assets.load()

SCREEN_SIZE = (700, 600)
VIEWPORT_SIZE = (192, 176)
BACKGROUND_COLOR = BLACK
FPS = 60

def main():
    clock = time.Clock()
    screen = display.set_mode(SCREEN_SIZE, RESIZABLE)
    viewport = viewports.Fit(VIEWPORT_SIZE, True)
    stage = menu.Menu(viewport.surface)

    while not events.check(events.QUIT):
        events.update()
        change = events.check(events.CHANGE_STAGE)
        if change:
            stage = change.stage
        clock.tick(FPS)
        stage.act(viewport.surface, clock.get_time())

        viewport.display(screen)
        display.flip()
    quit()
    exit()

if __name__ == "__main__":
    main()
