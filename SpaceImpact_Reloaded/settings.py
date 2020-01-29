# Class to store all the alien invasion settings - Appearance settings

class Settings():

    def __init__(self):
        
        #Initialize the games settings

        self.screen_width = 1200
        self.screen_height = 800
        self.rbg_color = (230, 230, 230)

        #Ship Speed Setting
        self.ship_speed_factor = 2.813

        #Bullet Settings
        self.bullet_speed_factor = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60