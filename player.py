import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """A class to represent a single player."""

    def __init__(self, gb_game):
        """Initialize the player and set its starting position."""
        super().__init__()
        self.screen = gb_game.screen
        self.settings = gb_game.settings
        self.screen_rect = gb_game.screen.get_rect()
    
        self.player_rect = pygame.Rect(
            0, 0, self.settings.player_width, self.settings.player_height
            )
        
        # Start each new player at the center of the screen.
        self.player_rect.center = self.screen_rect.center
        
        # Store a decimal value for the player's horizontal and vertical position.
        self.x = float(self.player_rect.x)
        self.y = float(self.player_rect.y)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the player's position based on the movement flag."""
        if self.moving_right and self.player_rect.right < self.screen_rect.right:
            self.player_rect.x += self.settings.player_speed
        if self.moving_left and self.player_rect.left > 0:
            self.player_rect.x -= self.settings.player_speed
        if self.moving_up and self.player_rect.top > 0:
            self.player_rect.y -= self.settings.player_speed
        if self.moving_down and self.player_rect.bottom < self.screen_rect.bottom:
            self.player_rect.y += self.settings.player_speed
        
    def blitme(self):
        """Draw the player at its current location."""
        pygame.draw.circle(self.screen,
                           self.settings.player_color,
                           self.player_rect.center,
                           self.settings.player_width/2)