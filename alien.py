#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, alien_invasion_game):
        super().__init__()
        self.screen = alien_invasion_game.screen

        self.image = pygame.image.load("assets/spaceArt/png/enemyShip.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
