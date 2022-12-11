import pygame
import Model
from eventmanager import *


class GraphicalView:

    def __init__(self, evManager, model):
        # connect to model
        self.model = model
        # manager set up
        self.evManager = evManager
        evManager.RegisterListener(self)
        # set up pygame window
        pygame.init()
        pygame.display.set_caption('Spain without the pain')
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.key.set_repeat(200, 20)
        self.clock = pygame.time.Clock()
        # title image
        self.titleimage = pygame.image.load('Title screen.png')
        # settings image
        self.settingsimage = pygame.image.load('Settings.png')
        # level images
        self.level1Image = pygame.image.load('Supermarket no man.png')
        self.level1ImageTeacher = pygame.image.load('Supermarket man.png')
        self.level2Image = pygame.image.load('Trains no man.png')
        self.level2ImageTeacher = pygame.image.load('Trains man.png')

    # Receive events posted to the message queue.
    def notify(self, event):
        if isinstance(event, QuitEvent):
            # shut down the pygame graphics
            quit()
        elif isinstance(event, TickEvent):
            currentstate = self.model.state.peek()
            if currentstate == Model.STATE_TITLE:
                self.renderTitle()
            elif currentstate == Model.STATE_SETTINGS:
                self.renderSettings()
            elif currentstate == Model.STATE_LEVEL1:
                self.renderLevel1()
            elif currentstate == Model.STATE_LEVEL2:
                self.renderLevel2()

    def renderTitle(self):
        self.screen.blit(self.titleimage, (0, 0))
        self.model.player.draw(self.screen)
        self.model.radio.setVolume(self.model.settingsbuttons[1].volume)
        self.clock.tick(18)
        pygame.display.update()

    def renderSettings(self):
        self.screen.blit(self.settingsimage, (0, 0))
        self.model.settingsbuttons[1].draw(self.screen)
        self.model.player.draw(self.screen)
        self.model.radio.setVolume(self.model.settingsbuttons[1].volume)
        self.clock.tick(18)
        pygame.display.update()

    def renderLevel1(self):
        self.model.radio.pause()
        self.screen.blit(self.level1ImageTeacher, (0, 0))
        self.clock.tick(18)
        pygame.display.update()

    def renderLevel2(self):
        self.model.radio.pause()
        self.screen.blit(self.level2ImageTeacher, (0, 0))
        self.clock.tick(18)
        pygame.display.update()
