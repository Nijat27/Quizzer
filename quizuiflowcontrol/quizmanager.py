import os
import datetime
import glob
from quizutils.quizparser import JSONQuizParser

class QuizManager:
    def __init__(self, quizfolder):
        """Initialize the QuizManager with the specified quiz folder."""
        self.quizfolder = quizfolder
        self.the_quiz = None
        self.quizzes = {}
        self.results = None
        self.quiztaker = ""

        if not os.path.exists(quizfolder):
            raise FileNotFoundError("The quiz folder doesn't exist!")

        self._build_quiz_list()

    def _build_quiz_list(self):
        """Method to build a list of quizzes from JSON files in the quiz folder."""
        pattern = os.path.join(self.quizfolder, '*.json')
        json_files = glob.glob(pattern)

        for i, f in enumerate(json_files):
            parser = JSONQuizParser()
            self.quizzes[i + 1] = parser.parse_quiz(f)
            # if f.is_file():
            #     print(f)
            #     parser = JSONQuizParser()
            #     self.quizzes[i + 1] = parser.parse_quiz(f.path)

    def list_quizzes(self):
        """Display a list of all available quizzes."""
        for k, v in self.quizzes.items():
            print(f"({k}): {v.name}")

    def take_quiz(self, quizid, username):
        """Take a quiz with the given ID and record results for the specified username."""
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()
        return self.results

    def print_results(self):
        """Print the results of the quiz taken by the user."""
        self.the_quiz.print_results(self.quiztaker)

    def save_results(self):
        """Save the results of the quiz in a file."""
        today = datetime.datetime.now()
        filename = f"QuizResults_{today.year}_{today.month}_{today.day}.txt"
        n = 1
        while os.path.exists(filename):
            filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
            n += 1

        path_cur = os.getcwd()
        path_result = os.path.join(path_cur, 'db_results', filename)
        with open(path_result, "w") as f:
            self.the_quiz.print_results(self.quiztaker, f)
