import os
path_cur = os.getcwd()
path_db_quizzes = os.path.join(path_cur, 'db_quizzes')
# print(path_db_quizzes)

from quizuiflowcontrol.quizmanager import QuizManager

class QuizApp:
    def __init__(self):
        self.user_name = ""
        self.quiz_manager = QuizManager(path_db_quizzes)  # Replace with the actual path

    def run(self):
        self.display_welcome_message()
        self.ask_user_name()
        self.main_menu()

    def display_welcome_message(self):
        print("Welcome to the Quiz App")

    def ask_user_name(self):
        self.user_name = input("What is your name? ")
        print(f"Welcome, {self.user_name}!\n")

    def main_menu(self):
        while True:
            self.show_menu_options()
            user_choice = input("Your selection? ")

            if not user_choice:
                self.display_error_message()
                continue

            user_choice = user_choice.upper()

            if user_choice == 'E':
                self.exit_app()
                break
            elif user_choice == 'L':
                self.list_quizzes()
            elif user_choice == 'T':
                self.take_quiz()
            else:
                self.display_error_message()

    def show_menu_options(self):
        print("Please make a selection")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit the App")

    def display_error_message(self):
        print("Not a valid selection. Try again!")

    def exit_app(self):
        print("Exiting the Quiz App. Goodbye!")

    def list_quizzes(self):
        self.quiz_manager.list_quizzes()

    def take_quiz(self):
        try:
            quiz_number = int(input("Enter the quiz number: "))
            if quiz_number in self.quiz_manager.quizzes:
                print(f"You have selected quiz {quiz_number}")
                results = self.quiz_manager.take_quiz(quiz_number, self.user_name)
                print("Quiz completed. Here are your results:")
                self.quiz_manager.print_results()
                self.quiz_manager.save_results()
            else:
                print("Invalid quiz number.")
        except ValueError:
            self.display_error_message()

# if __name__ == "__main__":
#     quiz_app = QuizApp()
#     quiz_app.run()
