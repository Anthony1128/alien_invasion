import pygame
from pygame.sprite import Sprite


# Creating alien class
class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # setting an image for alien and getting a rectangle of it
        self.image = pygame.image.load('images/alien_ship_smaller2.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    # draws an alien
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # checks if alien reached the edge
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    # moves an alien
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


