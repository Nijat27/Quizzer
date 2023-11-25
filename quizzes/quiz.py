from quizzes.quiz_parser import create_quiz_obj


class Quiz:
	def __init__(self, json_filename):
		self.list_question_obj = create_quiz_obj(json_filename)
		self.list_answers = []
		self.score = None
		self.time_start = None  # time when user start quiz
		self.list_time_at_ans = []  # list of time spending

	def log_answers(self, selected_ans, time_at_ans=None):
	"""
	Stores the answers from user.
	"""
		self.list_answers.append(selected_ans)
		self.list_time_at_ans.append(time_at_ans)


	def cal_score(self):
	"""
	Calculates score of the quiz session.

	Example.
	list_answers = ['A', 'B', 'C']
	list_time_at_ans = [T1, T2, T3]
	# find time for each question
	Q1T = T1 - self.time_start
	Q2T = T2 - T1
	Q3T = T3 - T2
	if 0-60secs, score_extr = ration 1/Q1T
	if > 60 secs, score_extr = 0

	# score the correctness
	compare answer in self.list_question_obj with list_answers
	if correct, score = 1, otherwise = 0
	
	add information in self.score, self.score_extr, self.time_used
	"""
		pass



	