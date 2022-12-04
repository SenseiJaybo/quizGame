import pygame
import sqlite3
from Main_class import *
from Player import *

# instantiate plater
p = Player(100, 100, 10)

# instantiate main class
m = Main()

# while loop to run program
running = True
while running:

    # look at all events
    for event in pygame.event.get():
        # check if the player is trying to exit the game
        m.checkExit(event)
        # update the player
        p.draw(m.screen)
        p.movement()
        p.borderCollision()
        p.animate()

    # update game window
    m.update()



