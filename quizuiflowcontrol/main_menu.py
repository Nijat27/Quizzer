import os
from quizuiflowcontrol.quizmanager import QuizManager

class QuizApp:
    """
    A class to manage the Quiz Application user interface and flow.

    Attributes:
        user_name (str): Stores the user's name.
        quiz_manager (QuizManager): Manages the quizzes including listing and taking quizzes.
    """

    def __init__(self):
        """
        Initializes the QuizApp with an empty username and sets up the quiz manager.
        """
        self.user_name = ""
        # Initialize QuizManager with the path to the quiz database
        self.quiz_manager = QuizManager(os.path.join(os.getcwd(), 'db_quizzes'))

    def run(self):
        """
        Starts the main loop of the application, handling the core workflow.
        """
        self.display_welcome_message()
        self.ask_user_name()
        self.main_menu()

    def display_welcome_message(self):
        """
        Displays a welcome message at the beginning of the application.
        """
        print("Welcome to the Quiz App")

    def ask_user_name(self):
        """
        Prompts the user to enter their name and stores it.
        """
        self.user_name = input("What is your name? ")
        print(f"Welcome, {self.user_name}!\n")

    def main_menu(self):
        """
        Handles the main menu, allowing the user to choose different actions.
        """
        while True:
            self.show_menu_options()
            user_choice = input("Your selection? ")

            if not user_choice:
                self.display_error_message()
                continue

            if user_choice.upper() == 'E':
                self.exit_app()
                break
            elif user_choice.upper() == 'L':
                self.list_quizzes()
            elif user_choice.upper() == 'T':
                self.take_quiz()
            else:
                self.display_error_message()

    def show_menu_options(self):
        """
        Displays the available menu options.
        """
        print("Please make a selection")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit the App")

    def display_error_message(self):
        """
        Displays an error message for invalid menu selections.
        """
        print("Not a valid selection. Try again!")

    def exit_app(self):
        """
        Closes the application with a goodbye message.
        """
        print("Exiting the Quiz App. Goodbye!")

    def list_quizzes(self):
        """
        Lists all the available quizzes using the QuizManager.
        """
        self.quiz_manager.list_quizzes()

    def take_quiz(self):
        """
        Facilitates the process of taking a quiz.
        """
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

# Uncomment the below lines to run the Quiz App
# if __name__ == "__main__":
#     quiz_app = QuizApp()
#     quiz_app.run()
