import pygame

class Block(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 70
        self.img = pygame.image.load("ghostpy/assets/groundM.png").convert_alpha()
        pygame.display.flip()

    def render(self, window):
        #pygame.draw.rect(window, (45, 52, 54), (self.x, self.y, self.width, self.height))
        window.blit(self.img, (self.x, self.y))