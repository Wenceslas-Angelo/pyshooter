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
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
