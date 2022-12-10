import pygame
from eventmanager import *
from Player import Player
from Settings import settingsbuttons
from Title import titlebuttons
from sound import Sound


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

    # Receive events posted to the message queue.
    def notify(self, event):
        # Called by an event in the message queue.
        if isinstance(event, QuitEvent):
            self.running = False
        if isinstance(event, StateChangeEvent):
            # pop request
            if not event.state:
                # false if no more states are left
                if not self.state.pop():
                    self.evManager.Post(QuitEvent())
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


# State machine constants
STATE_TITLE = 1
STATE_SETTINGS = 2
STATE_LEVEL1 = 3
STATE_LEVEL2 = 4


class StateMachine():
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
