import pygame
from eventmanager import *


class GameEngine:

    def __init__(self, evManager):

        self.evManager = evManager
        # add to list of active listeners
        evManager.RegisterListener(self)
        self.running = False

    def notify(self, event):
        # Called by an event in the message queue.
        if isinstance(event, QuitEvent):
            self.running = False

    def run(self):
        self.running = True
        # tell everyone to initialise
        self.evManager.Post(InitializeEvent())
        # post a new tick every frame
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)
            pygame.display.update()
