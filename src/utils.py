import pygame
import assets

class ViewportFit:
    def __init__(self, display, size):
        self.target = display
        self.size = size
        self.surface = pygame.Surface(self.size)
    def flip(self):
        scaled_size = self.__fit_size(self.target.get_size())
        scaled_pos = self.__center_fit(self.target.get_size(), scaled_size)
        scaled = pygame.transform.scale(self.surface, scaled_size)
        self.target.blit(scaled, scaled_pos)
    def __fit_size(self, windowSize):
        r_w = windowSize[0] / windowSize[1]
        r_i = self.size[0] / self.size[1]
        if r_w > r_i:
            size = (self.size[0] * windowSize[1]/self.size[1], windowSize[1])
        else:
            size = (windowSize[0], self.size[1] * windowSize[0]/self.size[0])
        return size
    def __center_fit(self, windowSize, scaleSize):
        return ((windowSize[0] - scaleSize[0]) / 2,
                (windowSize[1] - scaleSize[1]) / 2)

