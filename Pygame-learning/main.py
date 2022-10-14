import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
game_icon = pygame.image.load("picture/game_icon.png")
pygame.display.set_caption('My First Game')
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/pico-8.ttf", 25)

sky_surf = pygame.image.load("picture/graphics/sky.jpg").convert()
ground_surf = pygame.image.load("picture/graphics/ground.png").convert()

score_surf = test_font.render("Score", False, (150, 200, 100))
score_rect = score_surf.get_rect(center=(400, 50))

deda_surf = pygame.image.load("picture/enemy/deda.png").convert_alpha()
deda_rect = deda_surf.get_rect(topleft=(600, 197))

player_surf = pygame.image.load("picture/player/player_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 290))
    pygame.draw.rect(screen, "Black", score_rect)
    pygame.draw.rect(screen, "Black", score_rect, 10)

    screen.blit(score_surf, score_rect)
    deda_rect.x -= 4
    if deda_rect.right < 0:
        deda_rect.left = 800
    screen.blit(deda_surf, deda_rect)
    screen.blit(player_surf, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    # if player_rect.colliderect(enemy_deda_rect):
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos) == False:
    #     print("not collision")

    pygame.display.update()
    clock.tick(60)