import os
import glob
import json

from quizzes.quiz_parser import QuizParser

path_cur = os.getcwd()
# print(path_cur)
path_dbquizzes = os.path.join(path_cur, 'db_quizzes')
# print(path_dbquizzes)

class QuizManager:

	def __init__(self):
		pass

	def get_all_quiz_name(self):
		qp = QuizParser()
		list_quiz_name = list(qp.get_all_pair_qname_file().keys())
		return list_quiz_name