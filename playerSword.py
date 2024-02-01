from pygame.sprite import Sprite
import pygame

class PlayerSword(Sprite):
    """A class to represent a player sword."""
    
    def __init__(self, gb_game):
        """Initialize the player sword and set its starting position."""
        init = super().__init__()
        self.screen = gb_game.screen
        self.settings = gb_game.settings

        self.sword_rect = pygame.Rect(
            0, 0, self.settings.sword_width, self.settings.sword_height
            )
        
        # Start each new sword at the center of the player.
        self.sword_rect.center = gb_game.player.player_rect.center
        
    def update(self, player):
        """Update the sword's position based on the player's position."""
        self.sword_rect.right = player.rect.right
        self.sword_rect.centery = player.rect.centery
        
    def draw_sword(self):
        """Draw the sword at its current location."""
        pygame.draw.rect(
            self.screen, self.settings.sword_color,
            (self.sword_rect.x, self.sword_rect.y,
             self.settings.sword_width,
             self.settings.sword_height)
            )