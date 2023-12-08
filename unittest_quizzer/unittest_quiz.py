import os
import glob
import unittest
from quizutils.quiz import Quiz, Question, QuestionMC, QuestionTF, Answer
from quizutils.quizparser import JSONQuizParser



class TestQuiz(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Starting test: TestQuiz')

    
    @classmethod
    def tearDownClass(cls):
        print('Finished test: TestQuiz')

        
    def setUp(self):
        print("setUp")
        
        path_json_filename = os.path.join(os.getcwd(), 'db_quizzes')
        self.jsonfile_path = path_json_filename
        pattern = os.path.join(self.jsonfile_path, '*.json')
        self.jsonfiles = glob.glob(pattern)

        self.quizzes = {}
        for i, f in enumerate(self.jsonfiles):
            parser = JSONQuizParser()
            self.quizzes[i + 1] = parser.parse_quiz(f)
        
        self.quiztaker = "TestName"
#         self.the_quiz = self.quizzes[quizid]
#         self.results = self.the_quiz.take_quiz()
        
        
    def tearDown(self):
        print("tearDown")
        
        
    def test_print_header(self):
        no_min_quize = min(self.quizzes)
#         no_max_quize = max(self.quizzes)  # if want to test all quiz objects
        no_max_quize = 1
        for idx in range(no_min_quize, no_max_quize+1):
            quiz_obj = self.quizzes[idx]

            for qidx, q in enumerate(quiz_obj.questions[:1]):
                quiz_obj.print_header(qidx)
            
#         self.quiz_obj.score = 0 
#         self.quiz_obj.correct_count = 0 
#         self.quiz_obj.time_start = time.time() 
#         for idx, q in enumerate(self.quiz_obj.questions): 
#             q.is_correct = False 
#             self.print_header(idx) 
            
            
    def test_print_results(self):
        pass
        
    def test_take_quiz(self):
        pass
        
    def test_cal_score(self):
        pass
    
    
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




