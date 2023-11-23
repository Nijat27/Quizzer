import os
import glob
import json

path_cur = os.getcwd()
# print(path_cur)
path_dbquizzes = os.path.join(path_cur, 'db_quizzes')
# print(path_dbquizzes)

class QuizParser:

	def __init__(self):
		# self.quizname = quizname  # name of .json file
		pass 

	def get_all_pair_qname_file(self):

		# Use os.path.join to create the full path
		pattern = os.path.join(path_dbquizzes, '*.json')
		# Use glob to get all files matching the pattern
		json_files = glob.glob(pattern)

		dict_pair_qname_file = {}
		for json_file in json_files:
			f = open(json_file)
			data = json.load(f)
			qname = data['quizname']
			dict_pair_qname_file[qname] = json_file
			f.close()

		return dict_pair_qname_file
