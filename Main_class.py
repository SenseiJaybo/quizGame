import pygame


class Main:
    def __init__(self):
        pygame.init()
        # set a key to automatically repeat if it is held down
        pygame.key.set_repeat(200, 20)
        # create screen and clock
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def update(self):
        # set frame rate
        self.clock.tick(24)
        pygame.display.update()

    def checkExit(self, event):
        # exit if 'x' button pressed
        if event.type == pygame.QUIT:
            quit()
        # exit if 'ESC' pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
