from pygame import sprite

class Stage:
    def __init__(self, bg):
        self.bg = bg
        self.actors = sprite.Group()
    def act(self, surface, dt):
        self.actors.update(dt)
        self.actors.clear(surface, self.bg)
        self.actors.draw(surface)
