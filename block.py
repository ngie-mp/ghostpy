import pygame

class Block(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 50

    def render(self, window):
        pygame.draw.rect(window, (45, 52, 54), (self.x, self.y, self.width, self.height))