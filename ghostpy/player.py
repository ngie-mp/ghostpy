import pygame

class Player(object):
    def __init__(self, x, y, img="ghostpy/assets/ghost.png"):
        self.x = x
        self.y = y
        self.velocity = 0
        self.width = 64
        self.height = 64
        self.falling = True
        self.ground = False
        self.img = pygame.image.load(img).convert_alpha()
        pygame.display.flip()

    def jump(self):
        if self.ground == False:
            return
        self.velocity = 10
        self.ground = False

    def collision(self, x1, y1, w1, h1, x2, y2, w2, h2):
        if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:

            return True

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:

            return True

        elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:

            return True

        elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:

            return True

        else:

            return False

    def update(self, gravity, blocklist):
        if self.velocity < 0:
            self.falling = True

        collision = False
        blockX, blockY = 0, 0

        for block in blocklist:

            collision = self.collision(self.x, self.y, self.width, self.height, block.x, block.y, block.width, block.height)

            if collision == True:
                blockX = block.x
                blockY = block.y
                break

        if collision == True:
            if self.falling == True:
                self.falling = False
                self.ground = True
                self.velocity = 0
                self.y = blockY - self.height


        if self.ground == False:
            self.velocity += gravity

        self.y -= self.velocity

    def render(self, window):
        window.blit(self.img, (self.x, self.y))
