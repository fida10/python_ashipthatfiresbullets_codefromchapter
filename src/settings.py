# Define a class named Settings
class Settings:
    # The constructor method for the Settings class
    def __init__(self):
        # Set the background color of the game screen to a light gray color
        # The color is specified as an RGB tuple where each value is between 0 and 255
        self.bg_color = (230, 230, 230)

        # Ship settings
        # Set the speed of the ship. The higher the number, the faster the ship will move
        self.ship_speed = 1.5

        # Bullet settings
        # Set the speed of the bullets. The higher the number, the faster the bullets will move
        self.bullet_speed = 20.0
        # Set the width of the bullets in pixels
        self.bullet_width = 3
        # Set the height of the bullets in pixels
        self.bullet_height = 15
        # Set the color of the bullets to a dark gray color
        # The color is specified as an RGB tuple where each value is between 0 and 255
        self.bullet_color = (60, 60, 60)

        # Set the maximum number of bullets that can be on the screen at the same time
        self.bullets_allowed = 3
