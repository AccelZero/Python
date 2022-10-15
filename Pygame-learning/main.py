import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
game_icon = pygame.image.load("picture/game_icon.png")
pygame.display.set_caption('DeDa running')
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/pico-8.ttf", 25)
game_active = True

sky_surf = pygame.image.load("picture/graphics/sky.jpg").convert()
ground_surf = pygame.image.load("picture/graphics/ground.png").convert()

score_surf = test_font.render("Score", False, (150, 200, 100))
score_rect = score_surf.get_rect(center=(400, 50))

deda_surf = pygame.image.load("picture/enemy/deda.png").convert_alpha()
deda_rect = deda_surf.get_rect(midbottom=(600, 291))

player_surf = pygame.image.load("picture/player/player_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                deda_rect.left = 800

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 290))
        pygame.draw.rect(screen, "Black", score_rect)
        pygame.draw.rect(screen, "Black", score_rect, 10)

        screen.blit(score_surf, score_rect)
        deda_rect.x -= 7
        if deda_rect.right < 0:
            deda_rect.left = 800
        screen.blit(deda_surf, deda_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

    # collision
        if deda_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("Pink")

    pygame.display.update()
    clock.tick(60)