import os
import glob
import json

from quizzes.quiz_parser import get_all_pair_qname_file
from quizzes.quiz import Quiz
import time


path_cur = os.getcwd()
# print(path_cur)
path_dbquizzes = os.path.join(path_cur, 'db_quizzes')
# print(path_dbquizzes)

class QuizManager:

	def __init__(self):
		pass

	def get_all_quiz_name(self):
		"""
		Provides the list of all quiz names in the quiz database.

		Returns
		-------
		list_quiz_name : list
			the list of quiz names
		"""
		list_quiz_name = list(get_all_pair_qname_file().keys())
		return list_quiz_name


	def run_quiz(self, json_filename='db_quizzes/english-speaking-small-talk_quiz.json'):
		"""
		Run the quiz after know a use give the quiz name

		Parameters
		----------
		json_filename : str
			the location of the quiz file in the db_quizzes.
			it should be "db_quizzes/<quiz_file>.json"
			using get_all_pair_qname_file function to get the 
			pairs of quizname and location of the quiz file .json
		"""

		quiz_obj = Quiz(json_filename)

		# set start time
		time_start = quiz_obj.log_start_time()

		# run quiz
		for idx_q, quest_obj in enumerate(quiz_obj.list_question_obj):

		    # get question from obj.
		    question = quest_obj.question
		    print(f'{idx_q+1})', question)
		    
		    # get choices from obj.
		    list_choices = quest_obj.choices
		    for idx_c, choice in enumerate(list_choices):
		        print(f'{idx_c+1})', choice)
		        
		    # get answer from user
		    answer_slctd = input("Your selection? ")
		    time_ans = time.time()

		    # convert number to choice text, support only integer
		    answer_slctd_covert = quest_obj.choices[int(answer_slctd)-1]
		    
		    # store the answer and time timestamp
		    quiz_obj.log_answers(answer_slctd_covert, time_ans)  # log the answer
		    
		    print('\n')

		# cal score
		score_user = quiz_obj.cal_score()
		print(f"Your quiz score is: {score_user:.02f} points")
