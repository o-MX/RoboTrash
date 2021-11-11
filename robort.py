import pygame, sys
import assets

class Robort:
    def __init__(self, y, front = True):
        self.pos = [7, y]
        self.size = (26, 15)
        self.sprite = None
        self.facing_front = not front
        self.rail = 0
        self.rotate()

    def move_left(self):
        if self.rail > 0:
            self.rail -= 1
            self.pos[0] -= 0.75 * self.size[0]

    def move_right(self):
        if self.rail < 2:
            self.rail += 1
            self.pos[0] += 0.75 * self.size[0]

    def rotate(self):
        self.facing_front = not self.facing_front
        if self.facing_front:
            subs_pos = pygame.Rect(0, 0, self.size[0], self.size[1])
        else:
            subs_pos = pygame.Rect(self.size[0], 0, self.size[0], self.size[1])
        self.sprite = assets.player_sprite.subsurface(subs_pos)
