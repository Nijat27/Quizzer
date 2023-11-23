import os
import glob
import json

path_cur = os.getcwd()
# print(path_cur)
path_dbquizzes = os.path.join(path_cur, 'db_quizzes')
# print(path_dbquizzes)

class QuizParser:

	def __init__(self, quizname):
		self.quizname = quizname  # name of .json file
