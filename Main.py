import pygame
import sqlite3
from Main_class import *
from Player import *

# instantiate plater
p = Player(300, 300, 5)

# instantiate main class
m = Main()

# while loop to run program
running = True
while running:
    # draw background
    m.drawBackground(0)
    # update the player
    p.movement()
    p.borderCollision()
    p.animate(m.screen)

    # look at all events
    for event in pygame.event.get():
        # check if the player is trying to exit the game
        m.checkExit(event)

    # update game window
    m.update()
