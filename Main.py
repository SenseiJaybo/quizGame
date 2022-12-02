import pygame
import sqlite3
from Main_class import *

m = Main()
m.__init__()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

    m.update()
