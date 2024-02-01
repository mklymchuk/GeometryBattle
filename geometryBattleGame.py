import sys
import pygame

from settings import Settings
from player import Player
from enemy import Enemy
from playerCircleAttack import PlayerCircleAttack

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
        self.player_circle_attack = PlayerCircleAttack(self, self.player)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.player.update()
            self.enemy.update()
            self.player_circle_attack.update()
            self._check_collision_enemy_circle_attack()
            self._check_collision_player_enemy()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._terminate_game()
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
            self._terminate_game()
            
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
            
    def _check_collision_player_enemy(self):
        """Check for collisions between the player and the enemy."""
        if self.player.rect.colliderect(self.enemy.rect):
            self.settings.player_health -= 1
            self.enemy.rect.x = 0
            self.enemy.rect.y = 0
            print(self.settings.player_health)
            if self.settings.player_health <= 0:
                print("You died!")
                
    def _check_collision_enemy_circle_attack(self):
        """Check for collisions between the enemy and the circle attack."""
        dx = self.player_circle_attack.center[0] - self.enemy.rect.centerx
        dy = self.player_circle_attack.center[1] - self.enemy.rect.centery
        distance = (dx**2 + dy**2)**0.5

        if distance < self.player_circle_attack.radius:
            self.settings.enemy_health -= 1
            print(self.settings.enemy_health)
            if self.settings.enemy_health <= 0:
                print("Enemy died!")
            
    def _terminate_game(self):
        """Terminate the game."""
        pygame.time.delay(500)
        pygame.quit()
        sys.exit()
                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.enemy.draw_enemy()
        self.player_circle_attack.draw()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    gb = GeometryBattleGame()
    gb.run_game()