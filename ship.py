#!/usr/bin/env python3

import pygame

class Ship:
    def __init__(self, alien_invasion_game) -> None:
        self.screen = alien_invasion_game.screen
        self.screen_rect = alien_invasion_game.screen.get_rect()

        self.image = pygame.image.load("assets/Example_ships/6B.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.flag_moving = 0
        self.ship_speed = 6

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.flag_moving == 1 and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ship_speed
        elif self.flag_moving == -1 and self.rect.left > 0:
            self.rect.x -= self.ship_speed
        else:
            pass
