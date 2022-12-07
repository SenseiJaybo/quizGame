import pygame
import sqlite3
from Main_class import *
from Player import *
from Button_class import Button
from Title import Title
from State_machine import GameMachine
from Settings import Settings

# instantiate state machine
machine = GameMachine()

# instantiate settings
s = Settings(machine)

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

    # if changing settings
    elif machine.is_settings:
        # load settings page
        s.drawScene(m.screen)
        s.buttonChecks(p)
        s.buttons[1].draw(m.screen)
        # # delete later
        # pygame.draw.rect(m.screen, (0, 255, 0), s.buttons[0])
        # pygame.draw.rect(m.screen, (0, 255, 0), s.buttons[0])

        # update the player
        p.movement()
        p.borderCollision()
        p.animate(m.screen)

    # if leaving
    elif machine.is_leave:
        exit()
    # if in level 1
    elif machine.is_level1:
        print(1)
        machine.finishLevel1()
    # if in level 2
    elif machine.finishLevel2:
        print(2)
        machine.finishLevel2()

    # look at all events
    for event in pygame.event.get():
        # check if the player is trying to exit the game
        m.checkExit(event)

    # update game window
    m.update()

    # delete later
    print(machine.current_state)
