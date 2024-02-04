import pygame.font

class PlayerHealthBar:
    """A class to represent the player's health bar."""
    
    def __init__(self, gb_game):
        """Initialize the player's health bar."""
        self.screen = gb_game.screen
        self.settings = gb_game.settings
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the health bar.
        self.width, self.height = 200, 20
        self.bar_color = (0,255,0)
        self.outline_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the health bar's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = 20
        
        # Flag to track whether the health bar should be visible.
        self.visible = True
        
    def _prep_health(self):
        """Turn the health into a rendered image and center text on the health bar."""
        health_str = str(self.settings.player_health)
        self.health_image = self.font.render(health_str, True, self.outline_color, self.bar_color)
        self.health_image_rect = self.health_image.get_rect()
        self.health_image_rect.center = self.rect.center
        
    def draw_health_bar(self):
        """Draw the health bar."""
        if self.visible:
            self.screen.fill(self.outline_color, self.rect)
            self.screen.fill(self.bar_color, self.rect) 
            self._prep_health()