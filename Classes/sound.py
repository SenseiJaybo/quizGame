import pygame


class Sound:
    def __init__(self):
        # sound mixer
        pygame.mixer.init()
        pygame.mixer.music.load('SFX/2024_Sound_Of_The_Summer.mp3')
        # audio for listening section
        self.feedbackSounds = [pygame.mixer.Sound('SFX/Success.mp3'), pygame.mixer.Sound('SFX/Fail.mp3')]
        self.audio = []
        for i in range(1, 52):
            self.audio.append(pygame.mixer.Sound(f'Audio files/{i}.wav'))

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def setVolume(self, volume):
        # music
        pygame.mixer.music.set_volume(volume)
        # spanish audio
        for i in self.audio:
            i.set_volume(volume)
        # SFX
        for i in self.feedbackSounds:
            i.set_volume(volume)
