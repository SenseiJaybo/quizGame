import pygame


class Sound:
    def __init__(self):
        # sound mixer
        pygame.mixer.init()
        pygame.mixer.music.load('2024_Sound_Of_The_Summer.mp3')
        # audio for listening section
        self.audio = []
        for i in range(1, 52):
            self.audio.append(pygame.mixer.Sound(f'Audio files/{i}.wav'))

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def setVolume(self, volume):
        pygame.mixer.music.set_volume(volume)
