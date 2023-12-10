import unittest
from unittest.mock import patch, MagicMock
from quizuiflowcontrol.quizmanager import QuizManager

class TestQuizManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_quiz_1 = {
            "quizname": "General Knowledge Quiz",
            "description": "A general knowledge quiz",
            "category": "General",
            "questions": [
                {
                    "type": "mc",
                    "points": "1",
                    "text": "What is the capital of France?",
                    "answer": "Paris",
                    "choices": {"1": "Paris", "2": "London", "3": "Berlin", "4": "Rome"}
                },
                {
                    "type": "tf",
                    "points": "1",
                    "text": "The sky is blue.",
                    "answer": "True",
                }
            ]
        }

        cls.mock_quiz_2 = {
            "quizname": "Science Quiz",
            "description": "A basic science quiz",
            "category": "Science",
            "questions": [
                {
                    "type": "mc",
                    "points": "1",
                    "text": "Water boils at 100 degrees Celsius.",
                    "answer": "True",
                },
                {
                    "type": "tf",
                    "points": "1",
                    "text": "Light travels faster than sound.",
                    "answer": "True",
                }
            ]
        }

    @patch('os.path.exists', return_value=True)
    def setUp(self, mock_exists):
        """Set up a QuizManager instance for each test"""
        self.quiz_manager = QuizManager('mock_quiz_folder')

    def test_build_quiz_list(self):
        with patch('glob.glob', return_value=['quiz1.json', 'quiz2.json']), \
             patch('quizutils.quizparser.JSONQuizParser.parse_quiz', side_effect=[self.mock_quiz_1, self.mock_quiz_2]) as mock_parse_quiz:
            self.quiz_manager._build_quiz_list()
            self.assertEqual(len(self.quiz_manager.quizzes), 2)
            mock_parse_quiz.assert_has_calls([unittest.mock.call('quiz1.json'), unittest.mock.call('quiz2.json')])

    @patch('builtins.print')
    def test_list_quizzes(self, mock_print):
        # Assuming self.mock_quiz_1 and self.mock_quiz_2 have a 'quizname' attribute
        mock_quiz_1_obj = MagicMock()
        mock_quiz_1_obj.name = self.mock_quiz_1["quizname"]

        mock_quiz_2_obj = MagicMock()
        mock_quiz_2_obj.name = self.mock_quiz_2["quizname"]

        self.quiz_manager.quizzes = {1: mock_quiz_1_obj, 2: mock_quiz_2_obj}
        self.quiz_manager.list_quizzes()

        # Check that the expected print calls were made
        mock_print.assert_any_call("(1): General Knowledge Quiz")
        mock_print.assert_any_call("(2): Science Quiz")


    @patch.object(QuizManager, '_build_quiz_list')
    def test_take_quiz(self, mock_build_quiz_list):
        mock_build_quiz_list.return_value = None
        mock_quiz = MagicMock()
        self.quiz_manager.quizzes = {1: mock_quiz}
        self.quiz_manager.take_quiz(1, 'Test User')
        mock_quiz.take_quiz.assert_called_once()

    @patch('os.path.exists', return_value=False)
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_results(self, mock_open, mock_exists):
        mock_quiz = MagicMock()
        self.quiz_manager.quizzes = {1: mock_quiz}
        self.quiz_manager.the_quiz = mock_quiz
        self.quiz_manager.quiztaker = 'Test User'
        self.quiz_manager.save_results()
        mock_open.assert_called_once()
        mock_quiz.print_results.assert_called_with('Test User', unittest.mock.ANY)

if __name__ == '__main__':
    unittest.main()
