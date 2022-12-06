import pygame
import sqlite3
from Main_class import *
from Player import *
from Button_class import Button
from Title import Title
from State_machine import GameMachine

# instantiate state machine
machine = GameMachine()

# instantiate title
t = Title(machine)

# instantiate plater
p = Player(157, 482, 4)

# instantiate main class
m = Main()

# while loop to run program
running = True
while running:

    # if in title screen
    if machine.is_title:
        # draw background
        t.drawScene(m.screen)
        # check button presses
        t.buttonChecks(p.rect)
        # update the player
        p.movement()
        p.borderCollision()
        p.animate(m.screen)
    elif machine.is_leave:
        exit()

    # look at all events
    for event in pygame.event.get():
        # check if the player is trying to exit the game
        m.checkExit(event)

    # update game window
    m.update()
