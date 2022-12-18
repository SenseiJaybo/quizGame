import pygame


class Text:
    def __init__(self):
        # font object
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textImage = None
        self.textImage2 = None
        self.pointer = 0
        self.dialogue = None

    def draw(self, surface, x, y):
        # draws current rendered text image to screen
        surface.blit(self.textImage, (x, y))
        surface.blit(self.textImage2, (x, y + 50))

    def getDialogue(self, level, scene):
        # clear list
        self.dialogue = None
        # gets a list of dialogue for current state
        if scene == 'transcript':
            self.dialogue = level.transcript.search(level.level, level.stage)
        elif scene == 'dialogue':
            self.dialogue = level.dialogue.search(level.level, level.stage)

    def createTextImage(self):
        self.textImage = self.font.render(self.dialogue[self.pointer][0], True, (255, 255, 255))
        self.textImage2 = self.font.render(self.dialogue[self.pointer][1], True, (255, 255, 255))

    def nextLine(self):
        try:
            var = self.dialogue[self.pointer + 1]
            return True
        except:
            return False
