# Surface is the screen object - Part of the screen where game elements are displayed

import pygame                 # Modules that contain game building functionality

from pygame.sprite import Group     #what is a group?

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():

    pygame.init() 
    
    ai_settings = Settings()
    #Initialize background settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")


    ship = Ship(ai_settings, screen)

    bullets = Group()  #group to store bullets

    #rbg_color = (230, 230, 230)

    while True:                                         #Main game loop
        
        # Watch for keyboard & mouse events

        gf.check_events(ai_settings, screen, ship, bullets)                           #calls events function and handles user inputs   
        ship.update() 
        bullets.update()                                  #ship attributes
        gf.update_screen(ai_settings, screen, ship, bullets)     #Show recently drawn screen

run_game()