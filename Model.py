import pygame
from eventmanager import *


class GameEngine:

    def __init__(self, evManager):
        self.evManager = evManager
        # add to list of active listeners
        evManager.RegisterListener(self)
        self.running = False
        self.state = StateMachine()

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
        # tell everyone to initialise
        self.evManager.Post(InitializeEvent())
        # start state
        self.state.push(STATE_TITLE)
        # post a new tick every frame
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)
            pygame.display.update()


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
