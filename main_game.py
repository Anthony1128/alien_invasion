import pygame
from settings_game import Settings
from ship import Ship
import game_func as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


# start game function
def run_game():
    pygame.init()

    # display interface
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, 'Play')
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Creating game objects
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # cycle of displaying game events
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.upd_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.upd_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


# starting game
run_game()