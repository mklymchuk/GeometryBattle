class Settings:
    """A class to store all settings for Geometry Battle Game."""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        
        # Set the background color to palegreen #98FB98.
        self.bg_color = (152,251,152)
        
        # Player settings
        self.player_width = 50
        self.player_height = 50
        self.player_color = (0,0,0)
        self.player_speed = 1.00
        
        # Enemy settings
        self.enemy_width = 25
        self.enemy_height = 25
        self.enemy_color = (255,0,0)
        self.enemy_speed = 0.50
        
        # Sword settings
        self.sword_width = 5
        self.sword_height = 40
        self.sword_color = (0,0,0)
        self.sword_swing_speed = 0.10
        self.sword_rotation_speed = 0.10
        