import pygame, random
from pygame import *

def tabuleiro():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)


def colisão(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

fruta_posição = tabuleiro()
fruta = pygame.Surface((10, 10))
fruta.fill((255, 0, 0))

direção = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direção = UP
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                direção = DOWN
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direção = LEFT
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direção = RIGHT

    if colisão(snake[0], fruta_posição):
        fruta_posição = tabuleiro()
        snake.append((0, 0))

    if direção == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direção == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direção == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direção == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    tela.fill((0, 0, 0))
    tela.blit(fruta, fruta_posição)
    for pos in snake:
        tela.blit(snake_skin, pos)

    pygame.display.update()