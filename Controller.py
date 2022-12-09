import pygame
import Model
from eventmanager import *


# Handles keyboard input.
class Keyboard:

    def __init__(self, evManager, model):
        # connection to post messages to event queue
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model

    # Receive events posted to the message queue.
    def notify(self, event):

        if isinstance(event, TickEvent):
            # Called for each game tick. We check our keyboard presses here.
            for event in pygame.event.get():
                # handle window manager closing our window
                if event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                # handle key down events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())
                    else:
                        # post any other keys to the message queue for everyone else to see
                        self.evManager.Post(InputEvent(event.unicode, None))
