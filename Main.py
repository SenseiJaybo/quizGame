import pygame
import sqlite3
from Main_class import *
from Player import *
from Button_class import Button
from Title import Title

# instantiate title
t = Title()

# instantiate plater
p = Player(157, 482, 4)

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
