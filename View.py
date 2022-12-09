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
        self.smallfont = None


# recieve from message queue
def notify(self, event):
    if isinstance(event, InitializeEvent):
        self.initialize()
    elif isinstance(event, QuitEvent):
        # shut down the pygame graphics
        self.isinitialized = False
        pygame.quit()
    elif isinstance(event, TickEvent):
        self.renderall()
        # set fps to 18 frames per second
        self.clock.tick(18)


# draw the data from model
def renderall(self):
    if not self.isinitialized:
        return
    # clear display
    self.screen.fill((0, 0, 0))
    # draw some words on the screen
    somewords = self.smallfont.render(
        'The View is busy drawing on your screen',
        True,
        (0, 255, 0))
    self.screen.blit(somewords, (0, 0))
    # flip the display to show whatever we drew
    pygame.display.flip()


def initialize(self):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Spain without the pain')
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.clock = pygame.time.Clock()
    self.smallfont = pygame.font.Font(None, 40)
    self.isinitialized = True
    pygame.key.set_repeat(200, 20)
