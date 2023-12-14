import unittest
from unittest.mock import patch, MagicMock
from quizuiflowcontrol.quizmanager import QuizManager
from quizuiflowcontrol.main_menu import QuizApp

class TestQuizApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up TestQuizApp class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestQuizApp class...")

    def setUp(self):
        self.quiz_app = QuizApp()
        self.quiz_app.quiz_manager = MagicMock()
        self.quiz_app.quiz_manager.the_quiz = None
        self.quiz_app.quiz_manager.quizzes = {}  # Set quizzes to an actual dictionary


    def tearDown(self):
        self.quiz_app = None

    def test_initialization(self):
        self.assertEqual(self.quiz_app.user_name, "")
        self.assertIsNotNone(self.quiz_app.quiz_manager)
        self.assertIsNone(self.quiz_app.quiz_manager.the_quiz)
        self.assertIsInstance(self.quiz_app.quiz_manager.quizzes, dict)

    @patch('builtins.input', return_value="Test User")
    def test_ask_user_name(self, mock_input):
        self.quiz_app.ask_user_name()
        self.assertEqual(self.quiz_app.user_name, "Test User")
        self.assertNotEqual(self.quiz_app.user_name, "")
        self.assertTrue(isinstance(self.quiz_app.user_name, str))
        self.assertEqual(mock_input.call_count, 1)

    @patch('builtins.input', side_effect=["L", "E"])
    def test_main_menu_list_quizzes(self, mock_input):
        self.quiz_app.main_menu()
        self.quiz_app.quiz_manager.list_quizzes.assert_called_once()
        self.assertEqual(mock_input.call_count, 2)
        self.assertNotEqual(mock_input.call_count, 1)
        self.assertTrue(callable(self.quiz_app.quiz_manager.list_quizzes))

    @patch('builtins.input', side_effect=["T", "1", "E"])
    def test_main_menu_take_quiz(self, mock_input):
        self.quiz_app.quiz_manager.quizzes = {1: MagicMock()}  # Ensure there is a quiz to take
        self.quiz_app.main_menu()
        self.quiz_app.quiz_manager.take_quiz.assert_called_once_with(1, self.quiz_app.user_name)
        self.assertEqual(mock_input.call_count, 3)
        self.assertTrue(callable(self.quiz_app.quiz_manager.take_quiz))

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["X", "E"])
    def test_main_menu(self, mock_input, mock_print):
        self.quiz_app.main_menu()
        mock_print.assert_any_call("Please make a selection")
        mock_print.assert_any_call("(L): List quizzes")
        mock_print.assert_any_call("(T): Take a quiz")
        mock_print.assert_any_call("(E): Exit the App")
        self.assertEqual(mock_input.call_count, 2)

if __name__ == '__main__':
    unittest.main()
