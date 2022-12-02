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
        # exit if 'x' button pressed
        if event.type == pygame.QUIT:
            quit()
        # exit if 'ESC' pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

    # update game window
    m.update()
