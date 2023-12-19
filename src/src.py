import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion: 
    def __init__(self):
        pygame.init()
        self.settings_for_game = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings_for_game.screen_width = self.screen.get_rect().width
        self.settings_for_game.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien invasion remaster")
        self.clock = pygame.time.Clock()
        self.bg_color = (self.settings_for_game.bg_color)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while(True):
            self._check_events()
            self.ship.update()
            self._update_bullets()
            
            self._update_screen()
            self.clock.tick(60)
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """ Handles keydown (pressing a key) events """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        """ Handles keyup (releasing a key) events """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings_for_game.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()
        
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.draw_ship_blit()
        
        pygame.display.flip()
    
if __name__ == '__main__':
    game_instance = AlienInvasion()
    game_instance.run_game()