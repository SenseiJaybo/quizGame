import pygame


class Sprite:
    def __init__(self, x, y, scale, image='Sprites/cursor.png'):
        self.X = x
        self.Y = y
        # load image and scale it accordingly
        self.image = pygame.image.load(f'{image}')
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * scale, self.image.get_height() * scale))
        # collision box
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, (self.X, self.Y))
