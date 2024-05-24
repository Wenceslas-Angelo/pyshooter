import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("./assets/comet.png")
        self.rect = self.image.get_rect()
        self.damage = 20
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, self.game.screen.get_width()-200)
        self.rect.y = -random.randint(0, self.game.screen.get_height()-200)

    def remove(self):
        self.game.comet_event.all_comets.remove(self)
        if len(self.game.comet_event.all_comets) == 0:
            self.game.comet_event.reset_percent()
            self.game.start()

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= self.game.screen.get_height()-100:
            self.remove()
            if len(self.game.comet_event.all_comets) == 0:
                self.game.comet_event.reset_percent()
                self.game.comet_event.fall_mode = False
        if self.game.check_collision(self, self.game.all_players):
            self.remove()
            self.game.player.damage(self.damage)

