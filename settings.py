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
        self.player_speed = 2.00
        self.player_health = 10
        self.max_player_health = 10
        
        # Enemy settings
        self.enemy_width = 25
        self.enemy_height = 25
        self.enemy_color = (255,0,0)
        self.enemy_speed = 1.00
        self.enemy_health = 10
        self.initial_enemy_health = 10
        
        # Circle attack settings
        self.circle_attack_width = 100
        self.circle_attack_height = 100
        self.circle_attack_color = (0,0,255)
        self.circle_atack_damage = 1

        # Game active flag
        self.game_active = False
        