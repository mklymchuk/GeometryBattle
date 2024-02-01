from pygame.sprite import Sprite
import pygame

class PlayerSword(Sprite):
    """A class to represent a player sword."""
    
    def __init__(self, gb_game):
        """Initialize the player sword and set its starting position."""
        super().__init__()
        self.screen = gb_game.screen
        self.settings = gb_game.settings

        # Load the sword image and get its rect.
        self.original_image = pygame.image.load('resourses/weapon/sword.png')
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()

        # Start each new sword at the center of the player.
        self.rect.center = gb_game.player.rect.center

        # Store a rotation angle for the sword.
        self.angle = 0

    def update(self, player):
        """Update the sword's position and rotation based on the player's position."""
        # Attach the sword to the player.
        self.up_sword = self.image.get_width() / 12
        self.left_sword = self.image.get_height() / 12
        # Set the center of rotation to a point to the right of the player.
        rotation_center = (player.rect.right + self.up_sword, player.rect.centery + self.left_sword)

        # Rotate the sword image.
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=rotation_center)

        # Update the rotation angle.
        self.angle = (self.angle + self.settings.sword_rotation_speed) % -45

    def draw_sword(self):
        """Draw the sword at its current location."""
        self.screen.blit(self.image, self.rect)