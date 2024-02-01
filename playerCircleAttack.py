from pygame.sprite import Sprite
import pygame

class PlayerCircleAttack(Sprite):
    """A class to represent a single player circle attack."""
    
    def __init__(self, gb_game, player):
        """Initialize the player circle attack and set its starting position."""
        self.screen = gb_game.screen
        self.settings = gb_game.settings
        self.color = self.settings.circle_attack_color
        self.screen_rect = gb_game.screen.get_rect()
        self.player = player
        
        self.circle_attack_rect = pygame.Rect(
            0, 0, self.settings.circle_attack_width, self.settings.circle_attack_height
            )
        
        self.radius = 0
        self.growth_rate = 0.1 # Change this to control how fast the circle grows.
        
    def update(self):
        """Update the player circle attack's position and size."""
        self.center = self.player.rect.center
        if self.radius < self.settings.circle_attack_width:
            self.radius += self.growth_rate
        else:
            self.circle_repeat_attack()
            
    def circle_repeat_attack(self):
        """Reset the circle attack."""
        self.radius = 0
        
    def draw(self):
        """Draw the player circle attack."""
        pygame.draw.circle(self.screen, self.color, self.center, self.radius, 2)