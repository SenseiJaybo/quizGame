import pygame
from Button_class import Button


class Title:
    def __init__(self, machine):
        # load background
        self.image = pygame.image.load('Title screen.png')
        self.buttons = []
        # create all the buttons
        self.buttons.append(FirstLevelButton(517, 252, machine))
        self.buttons.append(SettingsButton(517, 557, machine))
        self.buttons.append(SecondLevelButton(517, 405, machine))
        self.buttons.append(ExitButton(517, 711, machine))

    def drawScene(self, surface):
        surface.blit(self.image, (0, 0))

    def buttonChecks(self, rect, surface):
        # check if any of the buttons are being pressed
        for i in self.buttons:
            if i.clicked(rect):
                break


class FirstLevelButton(Button):
    # level 1 button
    def __init__(self, x, y, machine):
        super().__init__(x, y)
        self.machine = machine

    # go to first level
    def action(self):
        self.machine.openLevel1()


class SecondLevelButton(Button):
    # level 2 button
    def __init__(self, x, y, machine):
        super().__init__(x, y)
        self.machine = machine

    # got to second level
    def action(self):
        self.machine.openLevel2()


class SettingsButton(Button):
    # settings scene
    def __init__(self, x, y, machine):
        super().__init__(x, y)
        self.machine = machine

    # go to settings
    def action(self):
        self.machine.openSettings()


class ExitButton(Button):
    # exit scene
    def __init__(self, x, y, machine):
        super().__init__(x, y)
        self.machine = machine

    # leave game
    def action(self):
        self.machine.leaveGame()
