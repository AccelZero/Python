import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
game_icon = pygame.image.load("picture/game_icon.png")
pygame.display.set_caption('My First Game')
pygame.display.set_icon(game_icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()