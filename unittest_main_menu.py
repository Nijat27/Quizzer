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
        with patch('builtins.print', MagicMock()) as mock_print, \
             patch.object(self.quiz_app.quiz_manager, 'list_quizzes', MagicMock()) as mock_list_quizzes:
            self.quiz_app.list_quizzes()
            mock_list_quizzes.assert_called_once()
            mock_print.assert_called()
            self.assertTrue(mock_print.call_count > 1)
            mock_print.assert_any_call("Available Quizzes:")


    def test_take_quiz(self):
        """Test the take_quiz function"""
        with patch('builtins.input', return_value='1'), \
             patch.object(self.quiz_app.quiz_manager, 'take_quiz', MagicMock()) as mock_take_quiz, \
             patch.object(self.quiz_app.quiz_manager, 'print_results', MagicMock()) as mock_print_results, \
             patch.object(self.quiz_app.quiz_manager, 'save_results', MagicMock()) as mock_save_results:
            self.quiz_app.take_quiz()
            mock_take_quiz.assert_called_with(1, self.quiz_app.user_name)
            mock_print_results.assert_called_once()
            mock_save_results.assert_called_once()
            self.assertIsInstance(self.quiz_app.user_name, str)


    def test_main_menu(self):
        """Test the main_menu function"""
        with patch('builtins.input', side_effect=['E']), \
             patch('builtins.print', MagicMock()) as mock_print:
            self.quiz_app.main_menu()
            mock_print.assert_any_call("Welcome to the Quiz App")
            mock_print.assert_any_call("Please make a selection")
            mock_print.assert_any_call("(L): List quizzes")
            mock_print.assert_any_call("(E): Exit the App")


if __name__ == '__main__':
    unittest.main()
