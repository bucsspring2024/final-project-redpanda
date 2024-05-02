import pygame

class HangmanAudio:
    def __init__(self, music_file):
        self.music_file = music_file

    def play_music(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()
    
    def play_effect(self):
        effect = pygame.mixer.Sound(self.music_file)
        
        effect.play()