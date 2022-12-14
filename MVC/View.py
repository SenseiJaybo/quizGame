import pygame
from MVC import Model
from MVC.eventmanager import *


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
        pygame.key.set_repeat(300, 20)
        self.clock = pygame.time.Clock()
        # title image
        self.titleimage = pygame.image.load('backgrounds/Title screen.png')
        # settings image
        self.settingsimage = pygame.image.load('backgrounds/Settings.png')
        # level images
        self.levelImagesTranscript = [1, pygame.image.load('backgrounds/Supermarket transcript.png'),
                                      pygame.image.load('backgrounds/Trains transcript.png')]
        self.levelImagesDialogue = [1, pygame.image.load('backgrounds/Supermarket man.png'),
                                    pygame.image.load('backgrounds/Trains man.png')]
        self.levelImagesQuiz = [1, pygame.image.load('backgrounds/Supermarket Quiz.png'), pygame.image.load(
            'backgrounds/Trains Quiz.png')]

    # Receive events posted to the message queue.
    def notify(self, event):
        if isinstance(event, QuitEvent):
            # shut down the pygame graphics
            quit()
        elif isinstance(event, AudioEvent):
            # pause previous sound and then play next one
            pygame.mixer.Sound.stop(self.model.radio.audio[self.model.index - 1])
            pygame.mixer.Sound.play(self.model.radio.audio[self.model.index])
            self.model.index += 1
        elif isinstance(event, AudioReplayEvent):
            pygame.mixer.Sound.stop(self.model.radio.audio[self.model.index - 1])
            pygame.mixer.Sound.play(self.model.radio.audio[self.model.index - 1])
        elif isinstance(event, TickEvent):
            currentState = self.model.state.peek()
            if currentState == Model.STATE_TITLE:
                self.renderTitle()
            elif currentState == Model.STATE_SETTINGS:
                self.renderSettings()
            elif currentState == Model.STATE_LEVEL1 or currentState == Model.STATE_LEVEL2:
                self.renderLevel()
            elif currentState == Model.STATE_TRANSCRIPT:
                self.renderTranscript()
            elif currentState == Model.STATE_QUIZ or currentState == Model.STATE_ANOTHERQUESTION:
                self.renderQuiz()

    def renderTitle(self):
        # unpause music
        self.model.radio.unpause()
        # draw background
        self.screen.blit(self.titleimage, (0, 0))
        # player
        self.model.player.borderCollision(self.screen)
        self.model.player.draw(self.screen)
        # update volume
        self.model.radio.setVolume(self.model.settingsbuttons[1].volume)
        # update screen
        self.clock.tick(18)
        pygame.display.update()

    def renderSettings(self):
        # draw background
        self.screen.blit(self.settingsimage, (0, 0))
        self.model.settingsbuttons[1].draw(self.screen)
        # player
        self.model.player.borderCollision(self.screen)
        self.model.player.draw(self.screen)
        # update volume
        self.model.radio.setVolume(self.model.settingsbuttons[1].volume)
        # update screen
        self.clock.tick(18)
        pygame.display.update()

    def renderLevel(self):
        # pause sound
        self.model.radio.pause()
        # draw background
        self.screen.blit(self.levelImagesDialogue[self.model.level.level], (0, 0))
        # draw text
        self.model.text.createTextImage()
        self.model.text.draw(self.screen, 130, 625)
        self.clock.tick(18)
        pygame.display.update()

    def renderTranscript(self):
        # draw background
        self.screen.blit(self.levelImagesTranscript[self.model.level.level], (0, 0))
        # draw text
        self.model.transcript.createTextImage()
        self.model.transcript.draw(self.screen, 130, 625)
        self.clock.tick(18)
        pygame.display.update()

    def renderQuiz(self):
        # draw background
        self.screen.blit(self.levelImagesQuiz[self.model.level.level], (0, 0))
        # update text input
        self.model.level.updateText(self.screen)
        self.model.level.createText()
        self.screen.blit(self.model.level.fontImage,
                         (self.model.level.midpoint - (self.model.level.fontImage.get_width() / 2), 500))
        # display feedback
        if self.model.level.playerAnswerFeedback and self.model.level.right:
            # right
            self.model.level.CorrectAnswer(self.screen)
            pygame.mixer.Sound.play(self.model.radio.feedbackSounds[0])
            self.model.level.pause = True
        elif self.model.level.playerAnswerFeedback and not self.model.level.right:
            # wrong
            self.model.level.NotQuite(self.screen)
            pygame.mixer.Sound.play(self.model.radio.feedbackSounds[1])
            self.model.level.pause = True
        self.clock.tick(18)
        pygame.display.update()
