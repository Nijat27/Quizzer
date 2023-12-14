import unittest
from unittest_quizzer.unittest_quiz import TestQuiz
from unittest_quizzer.unittest_quizparser import TestQuizParser
from unittest_quizzer.unit_test_main import TestQuizApp
from unittest_quizzer.unit_test_quizmanager import TestQuizManager


def test_suite():
    """Test suite contains all unittests from all modules.
    """
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestQuizApp('test_initialization'))
    suite.addTest(TestQuizApp('test_ask_user_name'))
    suite.addTest(TestQuizApp('test_main_menu_list_quizzes'))
    suite.addTest(TestQuizApp('test_main_menu_take_quiz'))
    suite.addTest(TestQuizApp('test_main_menu'))
    suite.addTest(TestQuizManager('test_initialization'))
    suite.addTest(TestQuizManager('test_build_quiz_list'))
    suite.addTest(TestQuizManager('test_list_quizzes'))
    suite.addTest(TestQuizManager('test_take_quiz'))
    suite.addTest(TestQuizParser('test_import_data'))
    suite.addTest(TestQuizParser('test_create_question_obj'))
    suite.addTest(TestQuizParser('test_parse_quiz'))
    suite.addTest(TestQuiz('test_print_header'))
    suite.addTest(TestQuiz('test_print_results'))
    # suite.addTest(TestQuiz('test_take_quiz'))  # take_quiz is required user input.
    suite.addTest(TestQuiz('test_cal_score'))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))


test_suite()
