import pygame
import Model
from eventmanager import *


class GraphicalView:

    def __init__(self, evManager, model):
        # init variables to be set later
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None


# receive from message queue
def notify(self, event):
    if isinstance(event, InitializeEvent):
        self.initialize()
    elif isinstance(event, QuitEvent):
        # shut down the pygame graphics
        self.isinitialized = False
        pygame.quit()
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
        # set fps to 18 frames per second
        self.clock.tick(18)


def renderTitle(self):
    if not self.isinitialized:
        return


def renderSettings(self):
    if not self.isinitialized:
        return


def renderLevel1(self):
    if not self.isinitialized:
        return


def renderLevel2(self):
    if not self.isinitialized:
        return


def initialize(self):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Spain without the pain')
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.clock = pygame.time.Clock()
    self.isinitialized = True
    pygame.key.set_repeat(200, 20)
