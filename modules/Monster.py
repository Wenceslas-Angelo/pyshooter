import pygame
import random
from modules.Animation import AnimateSprite


class Monster(AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 100)
        self.rect.y = 440 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 100)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)
            self.game.add_score(self.loot_amount)
        if self.game.comet_event.is_full_loaded():
            self.game.all_monsters.remove(self)
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x+10, self.rect.y-20, self.health, 5])

    def forward(self):
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)
        else:
            self.rect.x -= self.velocity
