import pygame
from modules.Comet import Comet


class CometFallEvent:

    def __init__(self, game):
        self.game = game
        self.percent = 0
        self.percent_speed = 5
        self.all_comets = pygame.sprite.Group()
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def meteor_fall(self):
        for i in range(1, 10):
            self.all_comets.add(Comet(self.game))

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.fall_mode = True
            self.meteor_fall()

    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height()-20, surface.get_width(), 10])
        pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height()-20, (surface.get_width()/100)*self.percent, 10])

