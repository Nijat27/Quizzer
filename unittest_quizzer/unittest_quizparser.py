import os
import glob

import unittest
from quizutils.quizparser import JSONQuizParser
from quizutils.quiz import Question, Answer, QuestionMC, QuestionTF


class TestQuizParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Starting test: TestQuizParser')

    
    @classmethod
    def tearDownClass(cls):
        print('Finished test: TestQuizParser')
    
    
    def setUp(self):
        print("setUp")
        path_json_filename = os.path.join(os.getcwd(), 'db_quizzes')
        self.jsonfile_path = path_json_filename
        pattern = os.path.join(self.jsonfile_path, '*.json')
        self.jsonfiles = glob.glob(pattern)

        self.parser = JSONQuizParser()
    
    def tearDown(self):
        print("tearDown")
        
    
    def test_import_data(self):
        
        for idx, jsonfile in enumerate(self.jsonfiles):
            
            data = self.parser.import_data(jsonfile)
            list_key = list(data.keys())
            list_key.sort()
            list_check_data = ['category', 'description', 'questions', 'quizname']

            # main
            self.assertListEqual(list_key, list_check_data)  # check imported data has same keys
            self.assertEqual(len(list_key), 4)  # check # of keys in the imported data

            # each question
            for q in data['questions']:
                list_choices = list(q['choices'].values())
                self.assertIn(q['type'], ['mc', 'tf'])  # check question type must has mc or tf
                self.assertEqual(q['points'].isnumeric(), True)  # check point can be convert to numeric
                self.assertGreater(len(q['text']), 0)  # check object has question text 
                self.assertIn(q['answer'], list_choices)  # check corrected answer is available in the list of choices
                
    
    def test_create_question_obj(self):
        for idx, jsonfile in enumerate(self.jsonfiles):
            data = self.parser.import_data(jsonfile)

            for quest in data['questions']:
                quest_obj = self.parser.create_question_obj(quest)

                if quest['type']=="mc":
                    self.assertIsInstance(quest_obj, QuestionMC)
                else :
                    self.assertIsInstance(quest_obj, QuestionTF)
                    
                self.assertIsNotNone(quest_obj.text)
                self.assertIsNotNone(quest_obj.correct_answer)
                self.assertIsNotNone(quest_obj.points)
                self.assertIsNotNone(quest_obj.is_correct)
                self.assertIsNone(quest_obj.log_response)
                self.assertIsNone(quest_obj.log_time_at_res)
                
    
    def test_parse_quiz(self):
        for idx, jsonfile in enumerate(self.jsonfiles[:1]):

            quiz_obj = self.parser.parse_quiz(jsonfile)
            self.assertIsNotNone(quiz_obj.name)
            self.assertIsNotNone(quiz_obj.description)

            self.assertEqual(type(quiz_obj.total_points), int)
            self.assertGreater(len(quiz_obj.questions), 0)
            
    
unittest.main(argv=[''], verbosity=2, exit=False)




