import pygame


class Sprite:
    def __init__(self, x, y, scale, image):
        self.X = x
        self.Y = y
        self.image = pygame.image.load(f'{image}')
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * scale, self.image.get_height() * scale))
        self.rect = self.image.get_rect()
        self.show = True

    def draw(self, surface):
        self.rect.move(self.X, self.Y)
        if self.show:
            surface.blit(self.image, (self.X, self.Y))

