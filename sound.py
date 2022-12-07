import pygame


class Sound:
    def __init__(self):
        # sound mixer
        pygame.mixer.init()
        pygame.mixer.music.load('2024_Sound_Of_The_Summer.mp3')

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def setVolume(self, volume):
        pygame.mixer.music.set_volume(volume)


