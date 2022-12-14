import Databases
import pygame_textinput
import pygame
import random


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
        self.manager = pygame_textinput.TextInputManager(validator=lambda i: len(i) <= 20)
        self.textinput = pygame_textinput.TextInputVisualizer(manager=self.manager)
        self.textinput.font_color = (255, 255, 255)
        self.textinput.cursor_color = (255, 255, 255)
        # Quiz set up
        self.pause = False
        self.playerAnswerFeedback = False
        self.right = True
        self.words = None
        self.currentQuestion = None
        self.currentWord = ''
        self.correct = ''
        self.answering = True
        self.indexes = [0, 1, 2, 3, 4]
        # word placement vars
        self.X = 768

    def updateText(self, surface):
        if self.answering:
            surface.blit(self.textinput.surface, (130, 625))

    def createText(self):
        self.fontImage = self.font.render(f'{self.currentWord}', True, (255, 255, 255), (155, 205, 151))

    def getQuestions(self):
        self.words = None
        self.words = (self.quiz.search(self.level, self.stage))

    def randomChoice(self):
        # reset if all questions asked
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

    def judgeAnswer(self):
        answer = self.textinput.value
        if answer.upper() == self.correct:
            self.right = True
        else:
            self.right = False

    def wait(self):
        # 4.5 seconds
        pygame.time.wait(4500)

    def NotQuite(self, surface):
        notquite = self.font.render(f'{self.correct.lower()}', True, (255, 0, 0))
        surface.blit(notquite, (self.X - (notquite.get_width() / 2), 300))

    def CorrectAnswer(self, surface):
        correct = self.font.render('correct!', True, (0, 255, 0))
        surface.blit(correct, (620, 300))
