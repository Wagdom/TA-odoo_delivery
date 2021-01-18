import pygame

# khai bao cac phim su dung
from pygame.locals import (
        K_DOWN,
        K_UP,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT
)

pygame.init()
# khai bao khung chuong trinh
screen = pygame.display.set_mode((800, 600))
running = True
# dat ten cho chuong trinh
pygame.display.set_caption("Uni")
# dat icon cho chuong trinh
icon = pygame.image.load("groundhog.png")
# bắt buộc là file png
pygame.display.set_icon(icon)
# chay vong while de chuong trinh duy tri

# Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))

while running:
    #RGB - Red-Green_Blue
    screen.fill((0, 0, 0))
    playerX += 0.1
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()
