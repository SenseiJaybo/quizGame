import pygame
from Sprite import *
from Main_class import *

m = Main()


class Player(Sprite):
    def __init__(self, x, y, scale):
        # init using Sprite class method
        super().__init__(x, y, scale)
        self.speed = 5
        # load images for the walk cycles
        self.walkRight = [pygame.image.load('adventurer-run-00.png'), pygame.image.load('adventurer-run-01.png'),
                          pygame.image.load('adventurer-run-02.png'), pygame.image.load('adventurer-run-03.png'),
                          pygame.image.load('adventurer-run-04.png'), pygame.image.load('adventurer-run-05.png')]
        self.walkLeft = [pygame.image.load('adventurer-run-00L.png'), pygame.image.load('adventurer-run-01L.png'),
                         pygame.image.load('adventurer-run-02L.png'), pygame.image.load('adventurer-run-03L.png'),
                         pygame.image.load('adventurer-run-04L.png'), pygame.image.load('adventurer-run-05L.png')]
        self.idle = pygame.image.load('cursor.png')
        # variable to keep track of the animation cycle
        self.walkCount = 0
        # variable to keep track of what direction the player is moving in
        self.left = False
        self.right = False

    def movement(self):
        # check for colliding with screen boundary
        if not self.borderCollision():
            # look at all keys being pressed
            keys = pygame.key.get_pressed()
            # check for both left and right being pressed
            if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                self.right = False
                self.left = False
                self.walkCount = 0
            # move left
            elif keys[pygame.K_LEFT]:
                self.X -= self.speed
                self.left = True
                self.right = False
                self.walkCount += 1
            # move right
            elif keys[pygame.K_RIGHT]:
                self.X += self.speed
                self.left = False
                self.right = True
                self.walkCount += 1
            else:
                self.right = False
                self.left = False
                self.walkCount = 0

            # move up
            if keys[pygame.K_UP]:
                self.Y -= self.speed
            # move down
            elif keys[pygame.K_DOWN]:
                self.Y += self.speed

    def borderCollision(self):
        # check player's position in relation to screen border
        if self.X <= 0:
            return True
        elif self.Y <= 0:
            return True
        elif self.X >= m.screen.get_width():
            return True
        elif self.Y >= m.screen.get_height():
            return True
        else:
            return False

    def animate(self):
        # if player is at the end of cycle, reset to beginning
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        # both being pressed
        if self.right and self.left:
            self.image = self.idle
            self.walkCount = 0
        # loads walk cycle for left and right
        elif self.right:
            self.image = self.walkRight[self.walkCount // 4]
        elif self.left:
            self.image = self.walkLeft[self.walkCount // 4]
        # neither being pressed
        else:
            self.image = self.idle
            self.walkCount = 0

