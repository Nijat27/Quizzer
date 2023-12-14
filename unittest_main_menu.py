import unittest
from unittest.mock import patch, MagicMock
from quizuiflowcontrol.quizmanager import QuizManager
from quizuiflowcontrol.main_menu import QuizApp

class TestQuizApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Class level setup before all tests"""


    @classmethod
    def tearDownClass(cls):
        """Class level teardown after all tests"""


    def setUp(self):
        """Set up before each test"""
        self.quiz_app = QuizApp()

    def tearDown(self):
        """Tear down after each test"""


    def test_list_quizzes(self):
        """Test the list_quizzes function"""
        with patch('builtins.print', MagicMock()) as mock_print:
            self.quiz_app.list_quizzes()
            mock_print.assert_called()
            self.assertTrue(mock_print.call_count >= len(self.quiz_app.quiz_manager.quizzes))
            for quiz_id, quiz in self.quiz_app.quiz_manager.quizzes.items():
                mock_print.assert_any_call(f"({quiz_id}): {quiz.name}")

    def test_take_quiz(self):
        """Test the take_quiz function in QuizApp"""
        quiz_id = 1
        username = "Test User"
        self.quiz_app.user_name = username
        mock_result = (10, 5, 15)  # Expected return value
        mock_quiz = MagicMock()
        mock_quiz.take_quiz.return_value = mock_result

        with patch('builtins.input', return_value=str(quiz_id)), \
            patch.object(self.quiz_app.quiz_manager, 'quizzes', {quiz_id: mock_quiz}), \
            patch('builtins.print', MagicMock()):

            result = self.quiz_app.take_quiz()
            self.assertEqual(result, mock_result)


    def test_main_menu(self):
        """Test the main_menu function"""
        with patch('builtins.input', side_effect=['E']), \
             patch('builtins.print', MagicMock()) as mock_print:
            self.quiz_app.main_menu()
            mock_print.assert_any_call("Please make a selection")
            mock_print.assert_any_call("(L): List quizzes")
            mock_print.assert_any_call("(T): Take a quiz")
            mock_print.assert_any_call("(E): Exit the App")
            mock_print.assert_any_call("Exiting the Quiz App. Goodbye!")

if __name__ == '__main__':
    unittest.main()
