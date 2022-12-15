import pygame
import Model
from eventmanager import *
from Button_class import Button


# Handles keyboard input.
class Keyboard:

    def __init__(self, evManager, model):
        # connect to model
        self.model = model
        # connection to manager
        self.evManager = evManager
        evManager.RegisterListener(self)

    # Receive events posted to the message queue.
    def notify(self, event):
        if isinstance(event, TickEvent):
            # check state specific key presses
            currentstate = self.model.state.peek()
            if currentstate == Model.STATE_TITLE:
                self.keysTitle()
            elif currentstate == Model.STATE_SETTINGS:
                self.keysSettings()
            elif currentstate == Model.STATE_LEVEL1 or currentstate == Model.STATE_LEVEL2:
                self.keysLevel()
            elif currentstate == Model.STATE_TRANSCRIPT:
                self.keysTranscript()
            elif currentstate == Model.STATE_QUIZ or currentstate == Model.STATE_ANOTHERQUESTION:
                self.keysQuiz()
            # check non state specific button presses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                # handle key down events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())

    def keysTitle(self):
        # update the player
        self.model.player.movement()
        self.model.player.borderCollision()
        self.model.player.animate()
        # check button collisions
        for i, v in enumerate(self.model.titlebuttons):
            # level 1 button
            if i == 0:
                if v.clicked(self.model.player.rect):
                    self.evManager.Post(StateChangeEvent(Model.STATE_LEVEL1))
                    break
            # settings button
            elif i == 1:
                if v.clicked(self.model.player.rect):
                    self.evManager.Post(StateChangeEvent(Model.STATE_SETTINGS))
                    break
            # level 2 button
            elif i == 2:
                if v.clicked(self.model.player.rect):
                    self.evManager.Post(StateChangeEvent(Model.STATE_LEVEL2))
                    break
            # exit button
            elif i == 3:
                if v.clicked(self.model.player.rect):
                    self.evManager.Post(QuitEvent())
                    break

    def keysSettings(self):
        # update the player
        self.model.player.movement()
        self.model.player.borderCollision()
        self.model.player.animate()
        # check button collisions
        for i, v in enumerate(self.model.settingsbuttons):
            # back button
            if i == 0:
                if v.clicked(self.model.player.rect):
                    self.evManager.Post(StateChangeEvent(None))
                    break
            # volume slider
            elif i == 1:
                if v.clicked(self.model.player):
                    break

    def keysLevel(self):
        for event in pygame.event.get():
            # handle key down events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.evManager.Post(QuitEvent())
                # progress through dialogue
                if event.key == pygame.K_SPACE:
                    if self.model.text.nextLine():
                        self.model.text.pointer += 1
                    else:
                        # go to transcript scene
                        self.evManager.Post(StateChangeEvent(None))
                        self.evManager.Post(StateChangeEvent(Model.STATE_TRANSCRIPT))
                        self.evManager.Post(AudioEvent())
            if event.type == pygame.QUIT:
                self.evManager.Post(QuitEvent())

    def keysTranscript(self):
        for event in pygame.event.get():
            # handle key down events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.evManager.Post(QuitEvent())
                # progress through audio and transcript
                if event.key == pygame.K_r:
                    self.evManager.Post(AudioReplayEvent())
                if event.key == pygame.K_SPACE:
                    if self.model.transcript.nextLine():
                        self.evManager.Post(AudioEvent())
                        self.model.transcript.pointer += 1
                    else:
                        # go to quiz scene
                        self.evManager.Post(StateChangeEvent(None))
                        self.evManager.Post(StateChangeEvent(Model.STATE_QUIZ))
            if event.type == pygame.QUIT:
                self.evManager.Post(QuitEvent())

    def keysQuiz(self):
        # update text input
        events = pygame.event.get()
        self.model.level.textinput.update(events)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.evManager.Post(QuitEvent())
        # if enter answer, get another question or move on
        if keys[pygame.K_RETURN]:
            self.model.level.answering = False
            self.model.level.judgeAnswer()
            self.model.level.playerAnswerFeedback = True
        if self.model.level.pause:
            self.model.level.wait()
            # handle amount of answers
            if not self.model.level.randomChoice():
                if self.model.level.level == 1:
                    self.evManager.Post(StateChangeEvent(None))
                    if self.model.level.stage >= 3:
                        # if last stage
                        self.evManager.Post(StateChangeEvent(Model.STATE_TITLE))
                    else:
                        # if not last stage
                        self.evManager.Post(StateChangeEvent(Model.STATE_LEVEL1))
                elif self.model.level.level == 2:
                    self.evManager.Post(StateChangeEvent(None))
                    if self.model.level.stage >= 3:
                        # if last stage
                        self.evManager.Post(StateChangeEvent(Model.STATE_TITLE))
                    else:
                        # if not last stage
                        self.evManager.Post(StateChangeEvent(Model.STATE_LEVEL2))
            else:
                # another question
                self.evManager.Post(StateChangeEvent(None))
                self.evManager.Post(StateChangeEvent(Model.STATE_ANOTHERQUESTION))
