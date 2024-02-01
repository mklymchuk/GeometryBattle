import sys
import pygame

from settings import Settings
from player import Player
from enemie import Enemy
from playerSword import PlayerSword

class GeometryBattleGame:
    """Main class for the Geometry Battle game."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Geometry Battle Game")
        
        self.player = Player(self)
        self.enemy = Enemy(self)
        self.player_sword = PlayerSword(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.player.update()
            self.player_sword.update(self.player)
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._terminate_game(event)
            if event.type == pygame.KEYDOWN: 
                self._key_down_events(event)
            if event.type == pygame.KEYUP:
                self._key_up_events(event)
                    
    def _key_down_events(self, event):
        """A response to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True
        if event.key == pygame.K_q:
            self._terminate_game(event)
            
    def _key_up_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        if event.key == pygame.K_DOWN:
            self.player.moving_down = False
            
    def _terminate_game(self, event):
        """Terminate the game."""
        sys.exit()
                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.player_sword.draw_sword()
        self.enemy.draw_enemy()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    gb = GeometryBattleGame()
    gb.run_game()