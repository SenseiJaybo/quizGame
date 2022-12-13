import pygame
from eventmanager import *
from Player import Player
from Settings import settingsbuttons
from Title import titlebuttons
from sound import Sound
from Level import Level
from TextBox import Text
from Transcript import Transcript


class GameEngine:

    def __init__(self, evManager):
        # connect to manager
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.running = False
        self.state = StateMachine()
        # create player
        self.player = Player(157, 482, 4)
        # sound mixer
        self.radio = Sound()
        # title buttons
        self.titlebuttons = titlebuttons
        # settings buttons
        self.settingsbuttons = settingsbuttons
        # level init
        self.level = Level()
        # init text class
        self.text = Text()
        # init transcript
        self.transcript = Transcript()
        # index for audio files
        self.index = 0

    # Receive events posted to the message queue.
    def notify(self, event):
        # Called by an event in the message queue.
        if isinstance(event, QuitEvent):
            self.running = False
        if isinstance(event, StateChangeEvent):
            if event.state == STATE_TITLE:
                # reset stage
                self.level.stage = 0
            elif event.state == STATE_LEVEL1:
                self.setupStage(1)
            elif event.state == STATE_LEVEL2:
                self.setupStage(2)
            elif event.state == STATE_TRANSCRIPT:
                self.transcript.getDialogue(self.level)
            elif event.state == STATE_QUIZ:
                # init quiz
                self.level.getQuestions()
                self.level.randomChoice()
                self.resetQuizValues()
            elif event.state == STATE_ANOTHERQUESTION:
                self.resetQuizValues()

            # pop request
            if not event.state:
                # false if no more states are left
                if not self.state.pop():
                    pass
            else:
                # push a new state on the stack
                self.state.push(event.state)

    def run(self):
        self.running = True
        # start state
        self.state.push(STATE_TITLE)
        # start music
        pygame.mixer.music.play(-1)
        # post a new tick every frame
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)

    def setupStage(self, level):
        if self.level.stage == 0:
            if level == 1:
                self.index = 0
            elif level == 2:
                self.index = 29
        self.level.stage += 1
        # set up the level state
        self.text.pointer = 0
        self.transcript.pointer = 0
        self.level.level = level
        self.text.getDialogue(self.level)

    def resetQuizValues(self):
        self.level.textinput.value = ''
        self.level.answering = True
        self.level.playerAnswerFeedback = False
        self.level.pause = False


# State machine constants
STATE_TITLE = 1
STATE_SETTINGS = 2
STATE_LEVEL1 = 3
STATE_LEVEL2 = 4
STATE_TRANSCRIPT = 5
STATE_QUIZ = 6
STATE_ANOTHERQUESTION = 7



class StateMachine:
    def __init__(self):
        self.statestack = []

    # returns current state
    def peek(self):
        try:
            return self.statestack[-1]
        except IndexError:
            # empty stack
            return None

    # returns current state and removes it from stack
    def pop(self):
        try:
            self.statestack.pop()
            return len(self.statestack) > 0
        except IndexError:
            # empty stack
            return None

    # add new state to stack
    def push(self, state):
        self.statestack.append(state)
        return state
