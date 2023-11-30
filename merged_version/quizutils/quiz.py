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

    def print_header(self, idx):
        print("\n\n*******************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {idx+1}/{len(self.questions)}")
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
        for idx, q in enumerate(self.questions):
            q.is_correct = False
            self.print_header(idx)
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
        # print question and choices
        print(self.text)
        for a in self.answers:
            print(f"{a.name}) {a.text}")
        
        # get response
        while True:
            response = input("? ")

            # check response
            ## response should be number
            try:
                response_int = int(response)
            except:
                print("Sorry, that's not a valid response. Please input the number of choice.")
                print("Please try again.")
                continue

            ## range answer number
            no_choices = len(self.answers)
            if (response_int > no_choices)|(response_int<1):
               print(f"Sorry, that's not a valid response. The input should be the number between 0 to {no_choices}")
               print("Please try again.")
               continue 

            ## no reponse
            if not response:
                print("Sorry, that's not a valid response.")
                print("Please try again.")
            else:
                # get text of answer from answer number
                response_text = self.answers[response_int-1].text
                # print('response_text', response_text)
                # print('self.correct_answer', self.correct_answer)
                self.is_correct = response_text.lower() == self.correct_answer
                break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""
