# Importing necessary modules
import sys  # Provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter
import pygame  # Pygame is a set of Python modules designed for writing video games
# Importing the Settings class from the settings module
from settings import Settings
from ship import Ship  # Importing the Ship class from the ship module
from bullet import Bullet  # Importing the Bullet class from the bullet module

# The main class for the game


class AlienInvasion:
    # The constructor method for the class
    def __init__(self):
        pygame.init()  # Initialize all imported pygame modules
        self.settings_for_game = Settings()  # Create an instance of Settings

        # Create a display surface
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Get the width of the screen and store it in settings
        self.settings_for_game.screen_width = self.screen.get_rect().width
        # Get the height of the screen and store it in settings
        self.settings_for_game.screen_height = self.screen.get_rect().height

        # Set the title of the window
        pygame.display.set_caption("Alien invasion remaster")
        # Create a clock object to control the frame rate
        self.clock = pygame.time.Clock()
        # Set the background color
        self.bg_color = (self.settings_for_game.bg_color)
        # Create an instance of Ship
        self.ship = Ship(self)
        # Create a group to store all bullets
        self.bullets = pygame.sprite.Group()

    # Method to start the main loop for the game
    def run_game(self):
        # Start the main loop
        while (True):
            # Check for events
            self._check_events()
            # Update the ship's position
            self.ship.update()
            # Update the bullets' positions
            self._update_bullets()

            # Update the screen
            self._update_screen()
            # Limit the frame rate to 60 FPS
            self.clock.tick(60)

    # Method to check for events
    def _check_events(self):
        # Loop through all events
        for event in pygame.event.get():
            # If the event is QUIT, exit the program
            if event.type == pygame.QUIT:
                sys.exit
            # If the event is a key press
            elif event.type == pygame.KEYDOWN:
                # Check which key was pressed
                self._check_keydown_events(event)
            # If the event is a key release
            elif event.type == pygame.KEYUP:
                # Check which key was released
                self._check_keyup_events(event)

    # Method to handle key press events
    def _check_keydown_events(self, event):
        # If the right arrow key is pressed, move the ship to the right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # If the left arrow key is pressed, move the ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # If the 'q' key is pressed, exit the program
        elif event.key == pygame.K_q:
            sys.exit()
        # If the space bar is pressed, fire a bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # Method to handle key release events
    def _check_keyup_events(self, event):
        # If the right arrow key is released, stop moving the ship to the right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # If the left arrow key is released, stop moving the ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # Method to fire a bullet
    def _fire_bullet(self):
        # If the number of bullets is less than the maximum allowed
        if len(self.bullets) < self.settings_for_game.bullets_allowed:
            # Create a new bullet and add it to the bullets group
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # Method to update the bullets
    def _update_bullets(self):
        # Update the position of all bullets
        self.bullets.update()

        # Remove bullets that have left the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    # Method to update the screen
    def _update_screen(self):
        # Fill the screen with the background color
        self.screen.fill(self.bg_color)
        # Draw all bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the ship
        self.ship.draw_ship_blit()

        # Update the display
        pygame.display.flip()


# If this file is run (instead of imported), start the game
if __name__ == '__main__':
    # Create an instance of the game
    game_instance = AlienInvasion()
    # Start the game
    game_instance.run_game()
