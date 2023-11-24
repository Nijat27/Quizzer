import os
import glob
import json

path_cur = os.getcwd()
# print(path_cur)
path_dbquizzes = os.path.join(path_cur, 'db_quizzes')
# print(path_dbquizzes)

# class QuizParser:  # No need right now

def get_json_files():
	
	pattern = os.path.join(path_dbquizzes, '*.json')
	json_files = glob.glob(pattern)
	# print(json_files)

	return json_files


def get_all_pair_qname_file():
	json_files = get_json_files()
	dict_pair_qname_file = {}
	for json_file in json_files:
		f = open(json_file)
		data = json.load(f)
		qname = data['quizname']
		dict_pair_qname_file[qname] = json_file
		f.close()

	return dict_pair_qname_file
