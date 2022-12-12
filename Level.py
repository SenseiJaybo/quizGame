import Databases
import pygame_textinput
import pygame
import random
import TextBox


class Level:
    def __init__(self):
        # attributes to keep track of level state
        self.level = 0
        self.stage = 0
        # database connection
        self.quiz = Databases.QuizQuestions()
        self.dialogue = Databases.Dialogue()
        self.transcript = Databases.Transcript()
        # font object
        self.font = pygame.font.Font('freesansbold.ttf', 80)
        self.fontImage = None
        # text input set up
        self.manager = pygame_textinput.TextInputManager(validator=lambda i: len(i) <= 25)
        self.textinput = pygame_textinput.TextInputVisualizer(manager=self.manager)
        self.textinput.font_color = (255, 255, 255)
        self.textinput.cursor_color = (255, 255, 255)
        # Quiz set up
        self.words = None
        self.currentQuestion = None
        self.currentWord = ''
        self.correct = ''
        self.answering = True
        self.indexes = [0, 1, 2, 3, 4]

    def updateText(self, surface):
        if self.answering:
            surface.blit(self.textinput.surface, (130, 625))

    def createText(self):
        self.fontImage = self.font.render(f'{self.currentWord}', True, (255, 255, 255), (155, 205, 151))
        print(self.words)
        print(self.currentWord, self.correct)

    def getQuestions(self):
        self.words = None
        self.words = self.quiz.search(self.level, self.stage)

    def randomChoice(self):
        if len(self.indexes) == 0:
            self.indexes = [0, 1, 2, 3, 4]
            return False
        else:
            # random select from questions
            index = random.choice(self.indexes)
            self.currentQuestion = self.words[index]
            # remove choice from options
            self.indexes.remove(index)
            self.currentWord = self.currentQuestion[0]
            self.correct = self.currentQuestion[1]
            return True

    def judgeAnswer(self, surface):
        answer = self.textinput.value
        if answer.upper() == self.correct:
            self.CorrectAnswer(surface)
        else:
            self.NotQuite(surface)

    def NotQuite(self, surface):
        notquite = self.font.render(f'{self.correct}', True, (255, 0, 0))
        surface.blit(notquite, (500, 100))

    def CorrectAnswer(self, surface):
        correct = self.font.render('correct!', True, (0, 255, 0))
        surface.blit(correct, (500, 100))
