import unittest
from unittest_quizzer.unittest_quiz import TestQuiz
from unittest_quizzer.unittest_quizparser import TestQuizParser


def test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestQuizParser('test_import_data'))
    suite.addTest(TestQuizParser('test_create_question_obj'))
    suite.addTest(TestQuizParser('test_parse_quiz'))

    suite.addTest(TestQuiz('test_print_header'))
    suite.addTest(TestQuiz('test_print_results'))
    # suite.addTest(TestQuiz('test_take_quiz'))
    suite.addTest(TestQuiz('test_cal_score'))
    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


test_suite()


