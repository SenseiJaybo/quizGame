import pygame
import sqlite3
from Main_class import *

# load main class
m = Main()
m.__init__()

# while loop to run program
running = True
while running:

    # look at all events
    for event in pygame.event.get():
        # check if the player is trying to exit the game
        m.checkExit(event)

    # update game window
    m.update()



