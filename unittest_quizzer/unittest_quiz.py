#!/usr/bin/env python
# coding: utf-8

# In[1]:


# cd ..


# In[2]:


import os
import glob
import unittest
from quizutils.quiz import Quiz, Question, QuestionMC, QuestionTF, Answer
from quizutils.quizparser import JSONQuizParser


# In[25]:


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
#         pattern = os.path.join(self.jsonfile_path, '*.json')
        pattern = os.path.join(self.jsonfile_path, 'english-vocabulary-numbers-quiz.json')

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
        try:
            no_min_quize = min(self.quizzes)
            no_max_quize = max(self.quizzes)  # if want to test all quiz objects
#             no_max_quize = 1
            for idx in range(no_min_quize, no_max_quize+1):
                quiz_obj = self.quizzes[idx]

                for qidx, q in enumerate(quiz_obj.questions[:1]):
                    quiz_obj.print_header(qidx)
            
        except Exception as ex:
            print("Message:", ex)
            raise 
            
            
    def test_print_results(self):
        try:
            no_min_quize = min(self.quizzes)
            no_max_quize = max(self.quizzes)  # if want to test all quiz objects
#             no_max_quize = 1
            for idx in range(no_min_quize, no_max_quize+1):
                quiz_obj = self.quizzes[idx]
                quiz_obj.correct_count = 1
                quiz_obj.quiz_score = 1
                quiz_obj.quiz_score_ext = 1
                quiz_obj.quiz_score_final = 1
                 
                for qidx, q in enumerate(quiz_obj.questions):
                    q.text = "Test"
                    q.log_response = "MyAnswer"
                    quiz_obj.list_time_used.append(1)
                    quiz_obj.list_score.append(1)
                    quiz_obj.list_score_ext.append(1)
                    quiz_obj.list_score_final.append(1)

                quiz_obj.print_results(self.quiztaker)
                
                self.assertEqual(len(quiz_obj.questions), 10)
                self.assertEqual(len(quiz_obj.list_time_used), 10)
                self.assertEqual(len(quiz_obj.list_score), 10)
                self.assertEqual(len(quiz_obj.list_score_ext), 10)
                self.assertEqual(len(quiz_obj.list_score_final), 10)

        except Exception as ex:
            print("Message:", ex)
            raise 
            

    def test_cal_score(self):
        pass
    
    
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:





# In[ ]:




