import pygame
from pygame.sprite import Sprite


""" #Bullet manager """ 

class Bullet(Sprite):  

    def __init__(self, ai_settings, screen, ship):

        super(Bullet, self).__init__()  #Create bullet object at ships position
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) # Create a bullte rectangle at (0, 0) then place it at the ship

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y) #store bullet position as decimal

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    '''Move Bullet up the screen'''

    def update(self):  

        self.y -= self.speed_factor  #update bullet position
        self.rect.y = self.y #update rectangle position

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.color, self.rect) #draw bullet rectangle on screen
