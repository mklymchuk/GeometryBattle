import pygame.font

class GameOver:
    """A class to manage the game over screen."""
    def __init__(self, gb_game):
        """Initialize the game over screen."""
        self.screen = gb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gb_game.settings
        
        # Set the dimensions and properties of the game over screen.
        self.width, self.height = 200, 50
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the game over screen's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The game over message needs to be prepped only once.
        self._prep_game_over()
        
    def _prep_game_over(self):
        """Turn the game over message into a rendered image."""
        game_over_str = "Game Over"
        self.game_over_image = self.font.render(game_over_str, True, self.text_color, self.settings.bg_color)
        
        # Center the game over message.
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = self.rect.center
        
    def draw_game_over(self):
        """Draw the game over message to the screen."""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.game_over_image, self.game_over_rect)