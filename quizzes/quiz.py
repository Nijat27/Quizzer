from quizzes.quiz_parser import create_quiz_obj


class Quiz:
	def __init__(self, json_filename):
		self.list_question_obj = create_quiz_obj(json_filename)
		self.list_answers = []
		self.score = 0

	def log_answers(self, selected_ans):
	"""
	Stores the answers from user.
	"""
		self.list_answers.append(selected_ans)


	def log_scores(self):
	"""
	Calculates score of the quiz session.
	"""
		pass