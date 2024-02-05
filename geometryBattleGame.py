import sys
import pygame

from settings import Settings
from playButton import PlayButton
from player import Player
from playerHealthBar import PlayerHealthBar
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
        
        self.play_button = PlayButton(self, "Play")
        self.player = Player(self)
        self.player_health_bar = PlayerHealthBar(self)
        self.enemies = pygame.sprite.Group()
        self.enemy = Enemy(self)
        self.enemies.add(self.enemy)
        self.player_circle_attack = PlayerCircleAttack(self, self.player)
        
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.settings.game_active:    
                self.player.update()
                self.enemies.update()
                self.player_circle_attack.update()
                self._check_collision_enemy_circle_attack()
                self._check_collision_player_enemy()
            self._update_screen()
            
            self.clock.tick(60)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._terminate_game()
            if event.type == pygame.KEYDOWN: 
                self._key_down_events(event)
            if event.type == pygame.KEYUP:
                self._key_up_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN and self.play_button.visible:
                mouse_pos = pygame.mouse.get_pos()
                self._button_clicked(mouse_pos)
                    
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
            
    def _button_clicked(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.game_active = True
            self.play_button.visible = False
            
    def _check_collision_player_enemy(self):
        """Check for collisions between the player and the enemy."""
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.settings.player_health -= 1
                if self.settings.player_health <= 0:
                    print("You died!")
                
    def _check_collision_enemy_circle_attack(self):
        """Check for collisions between the enemy and the circle attack."""
        for enemy in self.enemies:
            dx = self.player_circle_attack.center[0] - enemy.rect.centerx
            dy = self.player_circle_attack.center[1] - enemy.rect.centery
            distance = (dx**2 + dy**2)**0.5

            if distance < self.player_circle_attack.radius:
                self.settings.enemy_health -= 1
                print(self.settings.enemy_health)
                if self.settings.enemy_health <= 0:
                    enemy.reset_enemy()
                    self.settings.enemy_health = self.settings.initial_enemy_health
                         
    def _terminate_game(self):
        """Terminate the game."""
        pygame.time.delay(500)
        pygame.quit()
        sys.exit()
                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.play_button.draw_button()
        if self.settings.game_active:
            self.player.blitme()
            self.player_health_bar.draw_health_bar()
            self.enemies.draw(self.screen)
            self.player_circle_attack.draw()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    gb = GeometryBattleGame()
    gb.run_game()