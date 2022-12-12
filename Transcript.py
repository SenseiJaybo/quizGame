import pygame
import TextBox


class Transcript(TextBox.Text):
    def getDialogue(self, level):
        # clear list
        self.dialogue = []
        # gets a list of dialogue for current state
        self.dialogue = level.transcript.search(level.level, level.stage)

    def createTextImage(self):
        self.textImage = self.font.render(self.dialogue[self.pointer][1], True, (255, 255, 255))
        self.textImage2 = self.font.render(self.dialogue[self.pointer][0], True, (255, 255, 255))
