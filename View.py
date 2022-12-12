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
        self.levelImages = [pygame.image.load('Supermarket no man.png'), pygame.image.load('Supermarket man.png'),
                            pygame.image.load('Trains man.png'), pygame.image.load('Trains no man.png')]

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
                self.renderLevel(1)
            elif currentstate == Model.STATE_LEVEL2:
                self.renderLevel(2)
            elif currentstate == Model.STATE_TRANSCRIPT:
                self.renderTranscript()
            elif currentstate == Model.STATE_QUIZ:
                self.renderQuiz()

    def renderTitle(self):
        self.screen.blit(self.titleimage, (0, 0))
        self.model.player.draw(self.screen)
        # update volume
        self.model.radio.setVolume(self.model.settingsbuttons[1].volume)
        self.clock.tick(18)
        pygame.display.update()

    def renderSettings(self):
        self.screen.blit(self.settingsimage, (0, 0))
        self.model.settingsbuttons[1].draw(self.screen)
        self.model.player.draw(self.screen)
        # update volume
        self.model.radio.setVolume(self.model.settingsbuttons[1].volume)
        self.clock.tick(18)
        pygame.display.update()

    def renderLevel(self, level):
        # pause sound
        self.model.radio.pause()
        # draw background
        self.screen.blit(self.levelImages[level], (0, 0))
        # draw text
        self.model.text.createTextImage()
        self.model.text.draw(self.screen, 130, 625)
        self.clock.tick(18)
        pygame.display.update()

    def renderTranscript(self):
        pass

    def renderQuiz(self):
        pass
