from Classes.Button_class import Button
import pygame


class Slider(Button):
    # volume slider
    def __init__(self, x, y):
        super().__init__(x, y, box_X=120, box_Y=120)
        # load image
        self.image = pygame.image.load('Sprites/knob.png')
        # attributes to calculate volume
        self.lowerBound = -262
        # furthest right position minus the width of the knob
        self.upperBound = 440
        self._volume = 0.6
        self.range = self.upperBound - self.lowerBound
        # set collision
        self.rect.update((445, 325), (635, 90))

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        if value > 2.0:
            self._volume = 2.0
        elif value < 0.0:
            self._volume = 0.0
        else:
            self._volume = value

    def setVolume(self):
        self.volume = (self.X - self.lowerBound) / self.range

    def clicked(self, player):
        self.isPressed = False
        # get keyboard input
        keys = pygame.key.get_pressed()
        # do something if the player is on button and pressing space
        if self.rect.colliderect(player.rect):
            if keys[pygame.K_SPACE]:
                self.isPressed = True

        if self.isPressed:
            # offset
            self.X = player.X - 575
            self.setVolume()
            return True
        else:
            return False


class BackButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y, box_X=300, box_Y=100)


settingsbuttons = [BackButton(75, 710), Slider(0, 17)]
titlebuttons = [Button(517, 252), Button(517, 557), Button(517, 405), Button(517, 711)]
