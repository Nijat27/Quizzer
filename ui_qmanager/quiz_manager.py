import os
import glob
import json

from quizzes.quiz_parser import get_all_pair_qname_file

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