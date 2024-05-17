import pygame
from modules.Player import Player
from modules.Monster import Monster


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.key_pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def check_collision(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)
