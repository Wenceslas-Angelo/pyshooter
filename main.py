import pygame
import math
from modules.Game import Game

pygame.init()

clock = pygame.time.Clock()

FPS = 30

bgImage = pygame.image.load("./assets/bg.jpg")

pygame.display.set_caption("Shooter Game")

screen = pygame.display.set_mode((1080, 620))

banner = pygame.image.load("./assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load("./assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.2)
play_button_rect.y = math.ceil(screen.get_height() / 1.7)

game = Game(screen)

running = True

while running:
    screen.blit(bgImage, (0, -300))

    if game.is_playing:
        game.update()
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

    clock.tick(FPS)
