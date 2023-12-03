import os
import datetime
import glob
from quizutils.quizparser import JSONQuizParser

class QuizManager:
    """
    Manages the quizzes, including listing, taking, and saving results of quizzes.

    Attributes:
        quizfolder (str): Path to the directory containing quiz files.
        the_quiz (Quiz): Currently selected quiz object.
        quizzes (dict): Dictionary mapping quiz IDs to quiz objects.
        results (Result): Results of the last taken quiz.
        quiztaker (str): Name of the user taking the quiz.
    """

    def __init__(self, quizfolder):
        """
        Initialize the QuizManager with a specific quiz folder path.

        Args:
            quizfolder (str): The path to the folder containing quiz files.

        Raises:
            FileNotFoundError: If the specified quiz folder does not exist.
        """
        self.quizfolder = quizfolder
        self.the_quiz = None
        self.quizzes = {}
        self.results = None
        self.quiztaker = ""

        # Check if the quiz folder exists
        if not os.path.exists(quizfolder):
            raise FileNotFoundError("The quiz folder doesn't exist!")

        # Build the list of quizzes
        self._build_quiz_list()

    def _build_quiz_list(self):
        """
        Private method to build a list of quizzes from JSON files in the quiz folder.
        """
        # Define the pattern to search for JSON files
        pattern = os.path.join(self.quizfolder, '*.json')
        json_files = glob.glob(pattern)

        # Parse each JSON file and add to quizzes
        for i, f in enumerate(json_files):
            parser = JSONQuizParser()
            self.quizzes[i + 1] = parser.parse_quiz(f)

    def list_quizzes(self):
        """
        Display a list of all available quizzes to the user.
        """
        # Print each quiz in the list
        for k, v in self.quizzes.items():
            print(f"({k}): {v.name}")

    def take_quiz(self, quizid, username):
        """
        Facilitate taking a quiz by a user.

        Args:
            quizid (int): The ID of the quiz to take.
            username (str): The name of the user taking the quiz.

        Returns:
            Result: The results of the quiz.
        """
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()
        return self.results

    def print_results(self):
        """
        Print the results of the last taken quiz.
        """
        self.the_quiz.print_results(self.quiztaker)

    def save_results(self):
        """
        Save the results of the quiz in a uniquely named file.
        """
        # Generate a unique filename for the results
        today = datetime.datetime.now()
        filename = f"QuizResults_{today.year}_{today.month}_{today.day}.txt"
        n = 1
        while os.path.exists(filename):
            filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
            n += 1

        # Save the results in the specified file
        path_cur = os.getcwd()
        path_result = os.path.join(path_cur, 'db_results', filename)
        with open(path_result, "w") as f:
            self.the_quiz.print_results(self.quiztaker, f)
