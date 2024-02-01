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
        
        self.rect = pygame.Rect(
            0, 0, self.settings.enemy_width, self.settings.enemy_height
            )
        
        # Start each new enemy at a random position at the top of the screen.
        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = 0
        
        # Store a decimal value for the enemy's horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.player = gb_game.player

    def update(self):
        """Update the enemy's position to move towards the player."""
        # Calculate the direction vector from the enemy to the player.
        dx = self.player.rect.x - self.x
        dy = self.player.rect.y - self.y

        # Normalize the direction vector.
        magnitude = (dx**2 + dy**2)**0.5
        if magnitude > 0:
            dx /= magnitude
            dy /= magnitude

        # Move the enemy in the direction of the player.
        self.x += dx * self.settings.enemy_speed
        self.y += dy * self.settings.enemy_speed

        # Update the enemy's rect position.
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_enemy(self):
        """Draw the enemy at its current location."""
        pygame.draw.rect(
            self.screen, self.settings.enemy_color,
            (self.x, self.y,
             self.settings.enemy_width,
             self.settings.enemy_height)
            )