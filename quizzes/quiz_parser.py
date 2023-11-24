import os
import glob
import json

from quizzes.questions import MCQuestion, TFQuestion


path_cur = os.getcwd()
# print(path_cur)
path_dbquizzes = os.path.join(path_cur, 'db_quizzes')
# print(path_dbquizzes)

# class QuizParser:  # No need right now

def get_json_files():
	"""
	Get all .json files in the folder db_quizzes.
	"""
	pattern = os.path.join(path_dbquizzes, '*.json')
	json_files = glob.glob(pattern)
	# print(json_files)

	return json_files


def get_all_pair_qname_file():
	"""
	Get all quiz names with file names from .json file

	Returns
	-------
	dict_pair_qname_file : dict
		the pairs of quiz name and file name.
	"""
	json_files = get_json_files()
	dict_pair_qname_file = {}
	for json_file in json_files:
		f = open(json_file)
		data = json.load(f)
		qname = data['quizname']
		dict_pair_qname_file[qname] = json_file
		f.close()

	return dict_pair_qname_file


def create_quiz_obj(json_filename):
	"""
	Parse question data in the .json to question object
	and return list of the question objects.
	
	Parameters
	-------
	json_filename : str
		filename (json) that is pair with the quiz name.
	
	Returns
	-------
	list_question_obj : list
		list of the question objects.
	"""
	f = open(json_filename)
	qdata = json.load(f)
	f.close()

	# extract questions in the quiz
	list_question_obj = []
	for qt in qdata['questions']:
		if qt['type']=='tf':
			list_question_obj.append(TFQuestion(qt))
		elif qt['type']=='mc':
			list_question_obj.append(MCQuestion(qt))
		else:
			print('Question type is not accepted!!!')
			break

	return list_question_obj










