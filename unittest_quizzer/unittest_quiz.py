import os
import glob
import time
import unittest
from quizutils.quiz import Quiz, Question, QuestionMC, QuestionTF, Answer
from quizutils.quizparser import JSONQuizParser


class TestQuiz(unittest.TestCase):
    """
    The unittest object contain unittests of functions in the quiz.py file.
    """

    @classmethod
    def setUpClass(cls):
        # set a path of a JSON file
        path_json_filename = os.path.join(os.getcwd(), 'db_quizzes')
        jsonfile_path = path_json_filename
        # pattern = os.path.join(jsonfile_path, '*.json')  # check all .json files
        pattern = os.path.join(jsonfile_path, 'english-vocabulary-numbers-quiz.json')

        cls.jsonfiles = glob.glob(pattern)

    @classmethod
    def tearDownClass(cls):
        # clean a path of a JSON file
        cls.jsonfiles = None
        
    def setUp(self):
        # set up quiz object
        self.quizzes = {}
        for i, f in enumerate(self.jsonfiles):
            parser = JSONQuizParser()
            self.quizzes[i + 1] = parser.parse_quiz(f)
        
        self.quiztaker = "TestName"
        self.quiz_obj = self.quizzes[1]
        self.quiz_obj.time_start = time.time()
        self.quiz_obj.list_time_at_response = []
        self.quiz_obj.list_response = []
        self.quiz_obj.list_qanswer = []
        self.quiz_obj.list_qpoint = []
        list_makeanw = ['MyAnswer', 'three', 'MyAnswer', 'MyAnswer', 'MyAnswer',
                        'divided by', 'MyAnswer', 'equals', 'MyAnswer', 'MyAnswer',]
        
        for qidx, q in enumerate(self.quiz_obj.questions):
            self.quiz_obj.questions[qidx].log_response = "MyAnswer"
            self.quiz_obj.questions[qidx].log_time_at_res = time.time()
            if qidx==9:
                # generate 10 second of time spending for last answer
                self.quiz_obj.questions[qidx].log_time_at_res = time.time()+10
            self.quiz_obj.questions[qidx].log_response = list_makeanw[qidx]
        
    def tearDown(self):
        # clean set up data
        self.quizzes = None
        self.quiz_obj = None
        self.quiztaker = None
        
        
    def test_print_header(self):
        """Test the print_header function.
        """
        for qidx, q in enumerate(self.quiz_obj.questions[:1]):
            self.quiz_obj.print_header(qidx)

        self.assertEqual(len(self.quiz_obj.questions), 10)
        self.assertIsNotNone(self.quiz_obj.name)   
        self.assertIsNotNone(self.quiz_obj.description)
        self.assertEqual(self.quiz_obj.total_points, 10)

    def test_cal_score(self):
        """Test the cal_score function.
        """
        self.quiz_obj.cal_score()

        self.assertEqual(self.quiz_obj.quiz_score, 3.0)  # correct 3 questions
        self.assertEqual(self.quiz_obj.quiz_score_ext, 15.0)  # get 15 extra score, 5 per correct question
        self.assertEqual(self.quiz_obj.quiz_score_final, 18.0)  # total score
    
    
    def test_print_results(self):
        """Test the print_results function.
        """
        self.quiz_obj.cal_score()  # need calculate score first
        self.quiz_obj.print_results(self.quiztaker)

        self.assertEqual(len(self.quiz_obj.questions), 10)
        self.assertEqual(len(self.quiz_obj.list_time_used), 10)
        self.assertEqual(len(self.quiz_obj.list_score), 10)
        self.assertEqual(len(self.quiz_obj.list_score_ext), 10)
        self.assertEqual(len(self.quiz_obj.list_score_final), 10)

unittest.main(argv=[''], verbosity=2, exit=False)

