import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load("./assets/player.png");
        self.rect = self.image.get_rect()
        self.rect.y = 400


