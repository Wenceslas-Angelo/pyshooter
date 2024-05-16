import pygame

pygame.init()
bgImage = pygame.image.load("./assets/bg.jpg")
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 620))

running = True

while running:
    screen.blit(bgImage, (0, -300))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
