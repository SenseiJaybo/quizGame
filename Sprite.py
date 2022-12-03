import pygame


class Sprite:
    def __init__(self, x, y, scale, image):
        self.X = x
        self.Y = y
        # load image and scale it accordingly
        self.image = pygame.image.load(f'{image}')
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * scale, self.image.get_height() * scale))
        # collision box
        self.rect = self.image.get_rect()
        self.show = True

    def draw(self, surface):
        # makes sure that if the sprite moves then the collision box will move as well
        self.rect.move(self.X, self.Y)
        # draws the sprite if it is meant to be visible
        if self.show:
            surface.blit(self.image, (self.X, self.Y))

