import datetime
import sys

class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0

    def print_header(self):
        print("\n\n*******************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("*******************************************\n")

    def print_results(self, quiztaker, thefile=sys.stdout):
        print("*******************************************", file=thefile)
        print(f"RESULTS for {quiztaker}", file=thefile)
        print(f"Date: {datetime.datetime.today()}", file=thefile)
        print(f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file=thefile)
        print(f"SCORE: {self.score} points of possible {self.total_points}", file=thefile)
        print("*******************************************\n", file=thefile)

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False
            self.print_header()
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points
            print("------------------------------------------------\n")
        return (self.score, self.correct_count, self.total_points)

class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False

class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while True:
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")
            if len(response) == 0 or response[0].lower() not in ["t", "f"]:
                print("Sorry, that's not a valid response. Please try again.")
            else:
                self.is_correct = response[0].lower() == self.correct_answer
                break

class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while True:
            print(self.text)
            for a in self.answers:
                print(f"{a.name}) {a.text}")
            response = input("? ")
            if not response:
                print("Sorry, that's not a valid response. Please try again.")
            else:
                self.is_correct = response.lower() == self.correct_answer
                break

class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""
