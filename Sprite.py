import pygame
from Main_class import *
from Errors import CustomError

m = Main()


class Sprite:
    def __init__(self, x, y, scale, image='cursor.png'):
        # check that X is in screen confines
        if x >= m.screen.get_width() or x < 0:
            raise CustomError("X value must be within screen confines")
        else:
            self.X = x
        # check that Y is in screen confines
        if y >= m.screen.get_height() or y < 0:
            raise CustomError("Y value must be within screen confines")
        else:
            self.Y = y
        # load image and scale it accordingly
        self.image = pygame.image.load(f'{image}')
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * scale, self.image.get_height() * scale))
        # collision box
        self.rect = self.image.get_rect()
        self._show = True

    def draw(self, surface):
        # draws the sprite if it is meant to be visible
        if self.show:
            surface.blit(self.image, (self.X, self.Y))

    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, b):
        if type(b) == '<class \'bool\'>':
            self._show = b
        else:
            raise CustomError('Show attribute must be Boolean')

