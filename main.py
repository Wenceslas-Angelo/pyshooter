import pygame
from modules.Game import Game

pygame.init()
bgImage = pygame.image.load("./assets/bg.jpg")
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 620))
game = Game()
running = True

while running:
    screen.blit(bgImage, (0, -300))
    screen.blit(game.player.image, game.player.rect)

    if game.key_pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.key_pressed.get(pygame.K_LEFT):
        game.player.move_left()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False

