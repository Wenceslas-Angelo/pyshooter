import pygame
from modules.Player import Player
from modules.Monster import Monster
from modules.Comet_Event import CometFallEvent


class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent()
        self.all_monsters = pygame.sprite.Group()
        self.key_pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        self.all_monsters.draw(screen)

        if self.key_pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.key_pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def check_collision(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)
