import pygame 

class Ship: 
    def __init__(self, game_instance):
        self.screen = game_instance.screen
        self.settings = game_instance.settings_for_game
        self.screen_rect = game_instance.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x) #uses a floating point value for more precise positioning
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #above updates the floating point value, then below updates the rect value
        self.rect.x = self.x

    def draw_ship_blit(self):
        self.screen.blit(self.image, self.rect)
