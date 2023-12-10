from quizuiflowcontrol.quizmanager import *
from quizutils.quizparser import JSONQuizParser
from quizutils.quiz import *

class QuizTester:
    def __init__(self, quiz_folder):
        self.quiz_manager = QuizManager(quiz_folder)
        self.qparser_obj = JSONQuizParser()

    def list_quizzes(self):
        print("Available Quizzes:")
        self.quiz_manager.list_quizzes()

    def take_and_display_quiz(self, quiz_id, username):
        print(f"\n{username} is taking Quiz ID {quiz_id}")
        self.quiz_manager.take_quiz(quiz_id, username)
        print("\nQuiz Results:")
        self.quiz_manager.print_results()
        self.quiz_manager.save_results()
        print("Results saved.")

    def test_quiz_parsing(self, file_json):
        quiz_data = self.qparser_obj.import_data(file_json)
        print(quiz_data['quizname'])
        print(quiz_data['description'])
        print(quiz_data['questions'])

    def test_question_creation(self, question_data):
        question_obj = self.qparser_obj.create_question_obj(question_data)
        print(question_obj.text)
        print(question_obj.points)
        print(question_obj.correct_answer)
        print(question_obj.is_correct)
        print(question_obj.log_response)
        print(question_obj.log_time_at_res)

        question_obj.ask()
        print("Log Answer   :", question_obj.log_response)
        print("Time spending:", question_obj.log_time_at_res)
        print("Check the answer is correct? :", question_obj.is_correct)

    def run_quiz(self, file_json):
        quiz_obj = self.qparser_obj.parse_quiz(file_json)
        quiz_obj.quiztaker = "MyName"
        quiz_obj.take_quiz()

        quiz_obj.print_header(1)
        quiz_obj.print_header(2)
        quiz_obj.print_results("MyNameIS")


def main():
    quiz_tester = QuizTester('db_quizzes')

    # Test listing quizzes
    quiz_tester.list_quizzes()

    # Test taking a quiz
    quiz_tester.take_and_display_quiz(1, "Tester_name")

    # Test parsing quiz data
    file_json = 'db_quizzes/english-speaking-small-talk_quiz.json'
    quiz_tester.test_quiz_parsing(file_json)

    # Test question creation
    quiz_data = quiz_tester.qparser_obj.import_data(file_json)
    question_sample = quiz_data['questions'][1]
    quiz_tester.test_question_creation(question_sample)

    # Run a quiz
    quiz_tester.run_quiz(file_json)


if __name__ == '__main__':
    main()
