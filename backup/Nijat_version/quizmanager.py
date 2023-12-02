import os
import datetime
from quizparser import JSONQuizParser

class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        self.the_quiz = None
        self.quizzes = {}
        self.results = None
        self.quiztaker = ""

        if not os.path.exists(quizfolder):
            raise FileNotFoundError("The quiz folder doesn't exist!")

        self._build_quiz_list()

    def _build_quiz_list(self):
        for i, f in enumerate(os.scandir(self.quizfolder)):
            if f.is_file():
                parser = JSONQuizParser()
                self.quizzes[i + 1] = parser.parse_quiz(f.path)

    def list_quizzes(self):
        for k, v in self.quizzes.items():
            print(f"({k}): {v.name}")

    def take_quiz(self, quizid, username):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()
        return self.results

    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)

    def save_results(self):
        today = datetime.datetime.now()
        filename = f"QuizResults_{today.year}_{today.month}_{today.day}.txt"
        n = 1
        while os.path.exists(filename):
            filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
            n += 1
        with open(filename, "w") as f:
            self.the_quiz.print_results(self.quiztaker, f)