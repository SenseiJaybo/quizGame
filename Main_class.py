import pygame


class Main:
    def __init__(self):
        pygame.init()
        # set a key to automatically repeat if it is held down
        pygame.key.set_repeat(200, 20)
        # create screen and clock
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        # load background images in list
        self.backgrounds = [pygame.image.load('Title screen.png'), pygame.image.load('Settings.png'),
                            pygame.image.load('Supermarket no man.png'), pygame.image.load('Supermarket man.png'),
                            pygame.image.load('Trains no man.png'), pygame.image.load('Trains man.png'),
                            pygame.image.load('Quiz.png')]

    def drawBackground(self, i):
        # draw the background
        self.screen.blit(self.backgrounds[i], (0, 0))

    def update(self):
        # set frame rate
        self.clock.tick(18)
        pygame.display.update()

    def checkExit(self, event):
        # exit if 'x' button pressed
        if event.type == pygame.QUIT:
            quit()
        # exit if 'ESC' pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
