import pygame


# Settings of the Game
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = pygame.image.load('images/space_big.bmp')

        self.ship_limit = 1

        #bullets
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        #alien
        self.fleet_drop_speed = 10


        #speed_factors
        self.speedup_scale = 1.35
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    # settings that changes with every level
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    # applying dynamic settings
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
