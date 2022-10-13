import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
game_icon = pygame.image.load("picture/game_icon.png")
pygame.display.set_caption('My First Game')
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/pico-8.ttf", 25)

sky_surface = pygame.image.load("picture/graphics/sky.jpg")
ground_surface = pygame.image.load("picture/graphics/ground.png")
text_surface = test_font.render("My First Game", False, "Black")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 290))
    screen.blit(text_surface, (270, 50))

    pygame.display.update()
    clock.tick(60)