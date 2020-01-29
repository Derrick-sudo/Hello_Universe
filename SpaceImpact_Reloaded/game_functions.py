import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):     #handles user inouts

     for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            
            check_keydown_events(event, ai_settings, screen, ship, bullets)        #each key press is registered as a KEYDOWN event - checking for a KEYDOWN event
                
        elif event.type == pygame.KEYUP:

            check_keyup_events(event, ship)

            
def check_keydown_events(event, ai_setttings, screen, ship, bullets):

    if event.key == pygame.K_RIGHT:   #event.key attribute used to check if certain button is pressed
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:

        new_bullet = Bullet(ai_setttings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False 

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def update_screen(ai_settings, screen, ship, bullets):       #updates screen and image

    screen.fill(ai_settings.rbg_color)  #Set background colour 

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()                       #Place ship on background

    pygame.display.flip()