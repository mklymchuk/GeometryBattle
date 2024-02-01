from pygame.sprite import Sprite
from random import randint
import pygame

class Enemy(Sprite):
    """Code common to all enemies."""
    def __init__(self, gb_game):
        """Initialize the enemy and set its starting position."""
        super().__init__()
        self.screen = gb_game.screen
        self.settings = gb_game.settings
        self.screen_rect = gb_game.screen.get_rect()
        
        self.enemy_rect = pygame.Rect(
            0, 0, self.settings.enemy_width, self.settings.enemy_height
            )
        
        # Start each new enemy at a random position at the top of the screen.
        self.enemy_rect.x = randint(0, self.settings.screen_width)
        self.enemy_rect.y = 0
        
        # Store a decimal value for the enemy's horizontal and vertical position.
        self.x = float(self.enemy_rect.x)
        self.y = float(self.enemy_rect.y)
        
    def draw_enemy(self):
        """Draw the enemy at its current location."""
        pygame.draw.rect(
            self.screen, self.settings.enemy_color,
            (self.x, self.y,
             self.settings.enemy_width,
             self.settings.enemy_height)
            )