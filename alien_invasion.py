#!/usr/bin/env python3

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        # init
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
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
        pygame.display.flip()


if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
