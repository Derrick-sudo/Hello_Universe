import pygame
import os.path as path

root = path.dirname(__file__)

shipimage = 'ship.bmp'

image_path = path.join(root, 'images', shipimage)

#print(file_path)

class Ship():

    def __init__(self, ai_settings, screen):

        # Initialize the shit and set its starting point
        self.screen = screen
        self.ai_settings = ai_settings

        
        #Load ship image

        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()               #Put the ship (game element) in a rectangle or treat it like a rectangle
        self.screen_rect = screen.get_rect()            #Storing screens rectangle in screen_rect

        self.rect.centerx = self.screen_rect.centerx    #Making origin of ship equal to the origin of the rectangle
        self.rect.bottom = self.screen_rect.bottom      #Make bottom edges of the screens rect and the images rect equal

        self.center = float(self.rect.centerx) #store decimal value for the ships center position


        self.moving_right = False #Set default key value
        self.moving_left = False

    def update(self):   #manages ships position

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor  #move ship right continously when right button is pressed

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor  #move ship left continously when right button is pressed

        self.rect.centerx = self.center #centerx can only take integer values



    def blitme(self):

        self.screen.blit(self.image, self.rect)  #Draws ship at specified position on screen