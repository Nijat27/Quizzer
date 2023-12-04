from quizmanager import QuizManager

def main():
    # Path to the directory where quizzes are stored
    quiz_folder = '../db_quizzes'

    # Initialize QuizManager
    quiz_manager = QuizManager(quiz_folder)

    # List available quizzes
    print("Available Quizzes:")
    quiz_manager.list_quizzes()

    # Simulate user selecting a quiz and taking it
    selected_quiz_id = 1  # Assuming user selects quiz with ID 1
    username = "Nijat"
    print(f"\n{username} is taking Quiz ID {selected_quiz_id}")
    quiz_manager.take_quiz(selected_quiz_id, username)

    # Print the results
    print("\nQuiz Results:")
    quiz_manager.print_results()

    # Save the results
    quiz_manager.save_results()
    print("Results saved.")

if __name__ == '__main__':
    main()
