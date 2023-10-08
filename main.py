import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breaking Bricks -Rompiendo Ladrillos")

# brick
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
# coordenada x,y , ancho y altura
bricks = []
brick_rows = 6
# gap =>brecha
brick_gap = 10
# r= 7 //3 =>2
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
# lado del brecha
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))

# sphere
sphere = pygame.image.load('./images/sphere.png')
sphere = sphere.convert_alpha()
sphere_rect = sphere.get_rect()
sphere_start = (350, 250)
sphere_speed = (3.0, 3.0)
sx, sy = sphere_speed
sphere_served = False
sphere_rect.topleft = sphere_start

# paddle
pad = pygame.image.load('./images/paddle.png')
pad = pad.convert_alpha()
pad_rect = pad.get_rect()
pad_rect[1] = screen.get_height() - 100

clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))
    # show bricks
    for br in bricks:
        screen.blit(brick, br)

    # show paddle
    screen.blit(pad, pad_rect)
    # show sphere
    screen.blit(sphere, sphere_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        x -= 0.4 * dt
    if pressed[K_RIGHT]:
        x += 0.4 * dt
    if pressed[K_SPACE]:
        sphere_served = True

    if pad_rect[0] + pad_rect.width >= sphere_rect[0] >= pad_rect[0] and \
            sphere_rect[1] + sphere_rect.height >= pad_rect[1] and sy>0:
        sy *= -1
        continue

    # Top
    if sphere_rect[1] <= 0:
        sphere_rect[1] = 0
        sy *= -1

    # Bottom
    if sphere_rect[1] >= screen.get_height() - sphere_rect.height:
        sphere_rect[1] = screen.get_height() - sphere_rect.height
        sy *= -1

    # Left
    if sphere_rect[0] <= 0:
        sphere_rect[0] = 0
        sx *= -1

    # Right
    if sphere_rect[0] >= screen.get_width() - sphere_rect.width:
        sphere_rect[0] = screen.get_width() - sphere_rect.width
        sx *= -1

    pad_rect[0] = x
    if sphere_served:
        # movi sphere
        sphere_rect[0] += sx
        sphere_rect[1] += sy

    pygame.display.update()
pygame.quit()
