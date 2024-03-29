from pygame import mixer

class Audio:
    """A class to manage audio in the game."""
    def __init__(self):
        """Initialize the audio settings."""
        mixer.init()
        
    def play_background_music(self):
        """Play the background music."""
        mixer.music.load('source/audio/bg_music.wav')
        mixer.music.play(-1)
        
    def stop_background_music(self):
        """Stop the background music."""
        mixer.music.stop()
        
    def player_circle_attack_sound(self):
        """Play the sound of the player's circle attack."""
        player_circle_attack_sound = mixer.Sound('source/audio/circle_atack.wav')
        player_circle_attack_sound.play()
        
    def player_damaged_sound(self):
        """Play the sound of the player being damaged."""
        player_damaged_sound = mixer.Sound('source/audio/player_damage.wav')
        player_damaged_sound.play()