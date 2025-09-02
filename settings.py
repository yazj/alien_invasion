#!/usr/bin/env python3

class Settings:
    def __init__(self) -> None:
        self.screen_size = (1200, 800)
        self.background_color = (230, 230, 230)

        self.ship_speed = 6

        # bullet
        self.bullet_speed = 16.0
        self.bullet_width = 5
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
