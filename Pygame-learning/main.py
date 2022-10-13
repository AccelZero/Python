import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
game_icon = pygame.image.load("picture/game_icon.png")
pygame.display.set_caption('My First Game')
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/pico-8.ttf", 25)

sky_surface = pygame.image.load("picture/graphics/sky.jpg").convert()
ground_surface = pygame.image.load("picture/graphics/ground.png").convert()
text_surface = test_font.render("My First Game!", False, "Black")

enemy_deda_surface = pygame.image.load("picture/enemy/deda.png").convert_alpha()
enemy_deda_rect = enemy_deda_surface.get_rect(topleft = (600, 197))

player_surface = pygame.image.load("picture/player/player_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 290))
    screen.blit(text_surface, (265, 50))
    enemy_deda_rect.x -= 4
    if enemy_deda_rect.right < 0:
        enemy_deda_rect.left = 800
    screen.blit(enemy_deda_surface, enemy_deda_rect)
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(enemy_deda_rect):
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos) == False:
    #     print("not collision")

    pygame.display.update()
    clock.tick(60)