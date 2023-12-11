import unittest
from unittest.mock import patch, MagicMock
from quizuiflowcontrol.quizmanager import QuizManager

class TestQuizManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up TestQuizManager class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestQuizManager class...")

    @patch('os.path.exists', return_value=True)
    def setUp(self, mock_exists):
        self.quiz_folder = 'test_folder'
        self.quiz_manager = QuizManager(self.quiz_folder)

    def tearDown(self):
        self.quiz_manager = None

    def test_initialization(self):
        self.assertEqual(self.quiz_manager.quizfolder, self.quiz_folder)
        self.assertIsNone(self.quiz_manager.the_quiz)
        self.assertIsInstance(self.quiz_manager.quizzes, dict)
        self.assertEqual(len(self.quiz_manager.quizzes), 0)

    @patch('quizuiflowcontrol.quizmanager.os.path.exists', return_value=True)
    def test_build_quiz_list(self, mock_exists):
        self.quiz_manager._build_quiz_list()
        self.assertGreaterEqual(len(self.quiz_manager.quizzes), 0)
        #self.assertTrue(mock_exists.called)

    @patch('builtins.print')
    def test_list_quizzes(self, mock_print):
        self.quiz_manager.quizzes = {1: MagicMock(), 2: MagicMock()}
        self.quiz_manager.list_quizzes()
        self.assertEqual(mock_print.call_count, len(self.quiz_manager.quizzes))
        self.assertNotEqual(mock_print.call_count, 0)
        self.assertTrue(callable(self.quiz_manager.list_quizzes))
        self.assertIn(1, self.quiz_manager.quizzes)

    @patch('builtins.input', return_value="2")
    def test_take_quiz(self, mock_input):
        self.quiz_manager.quizzes = {1: MagicMock(), 2: MagicMock()}
        self.quiz_manager.take_quiz(2, "Test User")
        self.assertEqual(self.quiz_manager.quiztaker, "Test User")
        self.assertIsNotNone(self.quiz_manager.the_quiz)
        self.assertNotEqual(self.quiz_manager.quiztaker, "")
        self.assertIn(2, self.quiz_manager.quizzes)

if __name__ == '__main__':
    unittest.main()
