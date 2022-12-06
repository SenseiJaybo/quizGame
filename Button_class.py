import pygame.key

from Sprite import Sprite
from Player import Player


class Button(Sprite):
    def __init__(self, x, y, box_X=500, box_Y=120):
        super().__init__(x, y, 0)
        # create collision box
        self.rect.update((self.X, self.Y), (box_X, box_Y))
        self.isPressed = False

    # check collision
    def clicked(self, playerRect):
        self.isPressed = False
        # get keyboard input
        keys = pygame.key.get_pressed()
        # do something if the player is on button and pressing space
        if self.rect.colliderect(playerRect):
            if keys[pygame.K_SPACE]:
                self.isPressed = True

        if self.isPressed:
            self.action()

    # action the button does
    def action(self):
        print('a')
