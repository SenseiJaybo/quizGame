import Databases


class Level:
    def __init__(self):
        # attributes to keep track of level state
        self.level = 1
        self.stage = 1
        self.quiz = Databases.QuizQuestions()
        self.dialogue = Databases.Dialogue()
        self.transcript = Databases.Transcript()
