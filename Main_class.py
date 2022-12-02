import pygame


class Main:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(200, 20)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def update(self):
        self.clock.tick(24)
        pygame.display.update()
