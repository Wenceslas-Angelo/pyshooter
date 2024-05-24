import pygame
from modules.Player import Player
from modules.Mummy import Mummy
from modules.Alien import Alien
from modules.Comet_Event import CometFallEvent


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.key_pressed = {}
        self.score = 0
        self.font = pygame.font.Font("./assets/InputMono-Bold.ttf", 25)

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0

    def add_score(self, points=10):
        self.score += points

    def update(self):
        score_text = self.font.render(f"SCORE: {self.score}", 1, (0, 0, 0))
        self.screen.blit(score_text, (20, 20))

        self.screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(self.screen)

        self.player.update_animation()

        self.comet_event.update_bar(self.screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(self.screen)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(self.screen)
            monster.update_animation()

        self.all_monsters.draw(self.screen)

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.comet_event.all_comets.draw(self.screen)

        if self.key_pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < self.screen.get_width():
            self.player.move_right()
        elif self.key_pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def check_collision(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)
