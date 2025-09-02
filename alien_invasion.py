#!/usr/bin/env python3

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        # init
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._creat_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.flag_moving = 1
        elif event.key == pygame.K_LEFT:
            self.ship.flag_moving = -1
        elif event.key == pygame.K_q:
            # TODO ask if really want to quit
            sys.exit()
        # TODO continue fire
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.ship.flag_moving = -1
            else:
                self.ship.flag_moving = 0
        if event.key == pygame.K_LEFT:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.ship.flag_moving = 1
            else:
                self.ship.flag_moving = 0
                
    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

        
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _creat_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
