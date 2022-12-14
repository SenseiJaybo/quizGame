from Classes.Sprite import *


class Player(Sprite):
    def __init__(self, x, y, scale):
        # init using Sprite class method
        super().__init__(x, y, scale)
        self.lastDirectionRight = True
        self.scale = scale
        self.speed = 13
        # load images for the walk cycles
        self.walkRight = [pygame.image.load('Sprites/adventurer-run-00.png'), pygame.image.load(
            'Sprites/adventurer-run-01.png'),
                          pygame.image.load('Sprites/adventurer-run-02.png'), pygame.image.load(
                'Sprites/adventurer-run-03.png'),
                          pygame.image.load('Sprites/adventurer-run-04.png'), pygame.image.load(
                'Sprites/adventurer-run-05.png')]
        # scale images
        for i, v in enumerate(self.walkRight):
            self.walkRight[i] = pygame.transform.scale(v, (v.get_width() * scale, v.get_height() * scale))

        self.walkLeft = [pygame.image.load('Sprites/adventurer-run-00L.png'), pygame.image.load(
            'Sprites/adventurer-run-01L.png'),
                         pygame.image.load('Sprites/adventurer-run-02L.png'), pygame.image.load(
                'Sprites/adventurer-run-03L.png'),
                         pygame.image.load('Sprites/adventurer-run-04L.png'), pygame.image.load(
                'Sprites/adventurer-run-05L.png')]
        # scale images
        for i, v in enumerate(self.walkLeft):
            self.walkLeft[i] = pygame.transform.scale(v, (v.get_width() * scale, v.get_height() * scale))

        # load and scale idle sprites
        self.idle = pygame.image.load('Sprites/cursor.png')
        self.idleL = pygame.image.load('Sprites/cursorL.png')
        self.idle = pygame.transform.scale(self.idle, (self.idle.get_width() * scale, self.idle.get_height() * scale))
        self.idleL = pygame.transform.scale(self.idleL, (self.idleL.get_width() * scale, self.idleL.get_height() * scale))
        # variable to keep track of the animation cycle
        self.walkCount = 0
        # variable to keep track of what direction the player is moving in
        self.left = False
        self.right = False

    def movement(self):
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

        # if both
        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            pass
        # move up
        elif keys[pygame.K_UP]:
            self.Y -= self.speed
        # move down
        elif keys[pygame.K_DOWN]:
            self.Y += self.speed
        # makes sure that if the sprite moves then the collision box will move as well
        self.rect.update((self.X + 53, self.Y + 32), (23 * self.scale, 27 * self.scale))

    def borderCollision(self, surface):
        # check player's position in relation to screen border
        if self.X <= -11 * self.scale:
            self.X = -11 * self.scale
        if self.Y <= -7 * self.scale:
            self.Y = -7 * self.scale
        if self.X >= surface.get_width() - 40 * self.scale:
            self.X = surface.get_width() - 40 * self.scale
        if self.Y >= surface.get_height() - 37 * self.scale:
            self.Y = surface.get_height() - 37 * self.scale

    def animate(self):
        # if player is at the end of cycle, reset to beginning
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        # both being pressed or neither being pressed
        if self.right and self.left or not self.right ^ self.left:
            if self.lastDirectionRight:
                self.image = self.idle
            else:
                self.image = self.idleL
            self.walkCount = 0
        # loads walk cycle for left and right
        elif self.right:
            self.lastDirectionRight = True
            self.image = self.walkRight[self.walkCount // 3]
        elif self.left:
            self.lastDirectionRight = False
            self.image = self.walkLeft[self.walkCount // 3]

