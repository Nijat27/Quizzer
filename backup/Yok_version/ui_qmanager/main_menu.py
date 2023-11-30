class QuizApp:
    def __init__(self):
        self.user_name = ""

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
            elif user_choice == 'R':
                continue  # The menu will be displayed again at the start of the loop
            elif user_choice == 'L':
                self.list_quizzes()
            elif user_choice == 'T':
                self.take_quiz()
            else:
                self.display_error_message()

    def show_menu_options(self):
        print("Please make a selection")
        print("(R): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit the App")

    def display_error_message(self):
        print("Not a valid selection. Try again!")

    def exit_app(self):
        print("Exiting the Quiz App. Goodbye!")

    def list_quizzes(self):
        print("\nAvailable Quizzes Are: ")
        # Add logic to list available quizzes

    def take_quiz(self):
        try:
            quiz_number = int(input("Enter the quiz number: "))
            print(f"You have selected quiz {quiz_number}")
            # Add logic to start the quiz
        except ValueError:
            self.display_error_message()

if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.run()
