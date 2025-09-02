#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, alien_invasion_game):
        super().__init__()
        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        self.image = pygame.image.load("assets/spaceArt/png/laserGreen.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = alien_invasion_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
