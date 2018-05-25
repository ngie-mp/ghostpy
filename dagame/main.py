import pygame
from ghostpy.player import Player
from ghostpy.block import Block

pygame.init()

gray = (45, 52, 54)

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Hello")

gravity = -0.5

clock = pygame.time.Clock()

player = Player(10, 150)

level1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

blocklist = []

for y in range(0, len(level1)):
    for x in range(0, len(level1[y])):
        if level1[y][x] == 1:
            blocklist.append(Block(x*70, y*31))


moveX, moveY = 0,0
game_loop = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 5
                player.img = pygame.image.load("ghostpy/assets/ghost.png").convert_alpha()
            elif event.key == pygame.K_LEFT:
                moveX = -5
                player.img= pygame.image.load("ghostpy/assets/ghost2.png").convert_alpha()

            elif event.key == pygame.K_UP:
                player.jump()
        pygame.display.flip()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveX = 0
            elif event.key == pygame.K_LEFT:
                moveX = 0

    window.fill(gray)

    for block in blocklist:
        block.render(window)

    player.x += moveX
    player.update(gravity, blocklist)
    player.render(window)
    clock.tick(60)

    pygame.display.flip()

pygame.quit()
quit()