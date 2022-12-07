from Button_class import Button
import pygame


class Settings:
    def __init__(self, machine):
        # load background
        self.image = pygame.image.load('Settings.png')
        self.buttons = []
        # create all buttons
        self.buttons.append(BackButton(635, 721, machine))
        self.buttons.append(Slider(90, 17, machine))

    def drawScene(self, surface):
        surface.blit(self.image, (0, 0))

    def buttonChecks(self, rect):
        # check if any of the buttons are being pressed
        for i in self.buttons:
            if i.clicked(rect):
                break


class Slider(Button):
    # volume slider
    def __init__(self, x, y, machine):
        super().__init__(x, y, box_X=120, box_Y=120)
        # load image
        self.image = pygame.image.load('knob.png')
        self.machine = machine
        # attributes to calculate volume
        self.lowerBound = -262
        # furthest right position minus the width of the knob
        self.upperBound = 440
        self._volume = 1.0
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
        self.volume = (self.X - self.lowerBound) / (self.range / 2)

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
    # back button
    def __init__(self, x, y, machine):
        super().__init__(x, y, box_X=300, box_Y=100)
        self.machine = machine

    # go to first level
    def action(self):
        self.machine.goBack()
