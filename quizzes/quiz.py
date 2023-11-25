from quizzes.quiz_parser import create_quiz_obj

import time

class Quiz:
	def __init__(self, json_filename):
		self.list_question_obj = create_quiz_obj(json_filename)
		self.list_answers = []
		self.quiz_score = None
		self.list_score_final = None
		self.list_score = None
		self.list_score_ext = None
		self.time_start = None  # time when user start quiz
		self.list_time_at_ans = []  # list of time spending
		self.list_time_used = []  # list of time used


	def get_all_question_answers(self):
		list_quest_answer = []
		for question in self.list_question_obj:
			list_quest_answer.append(question.answer)
		return list_quest_answer


	def get_all_question_points(self):
		list_quest_points = []
		for question in self.list_question_obj:
			list_quest_points.append(question.points)
		return list_quest_points


	def log_start_time(self):
		self.time_start = time.time()
		return self.time_start


	def log_answers(self, selected_ans, time_at_ans):
		"""
		Stores the answers from user.
		"""
		self.list_answers.append(selected_ans)
		self.list_time_at_ans.append(time_at_ans)


	def cal_score(self):
		"""
		Calculates score of the quiz session.

		######################################################
		# I have done the main function but
		# This function need to add exception/check answer !!!
		######################################################
		"""

		# get time at each answering
		list_time_at_ans = self.list_time_at_ans

		# get time spending for each question in second unit
		for idx, _ in enumerate(list_time_at_ans):
		    if idx==0:
		        time_used = list_time_at_ans[idx] - self.time_start
		    else:
		        time_used = list_time_at_ans[idx] - list_time_at_ans[idx-1]
		        
		    self.list_time_used.append(time_used)
		
		# calculate score 
		## get corrected answers
		list_qanswer = self.get_all_question_answers()
		# print(list_qanswer)

		## get question points
		list_qpoint = self.get_all_question_points()
		# print(list_qpoint)

		## comapre the corrected answers with answers from a user
		list_score = []
		for idx, ans in enumerate(self.list_answers):
		    if ans==list_qanswer[idx]:
		        list_score.append(float(list_qpoint[idx]))
		    else:
		        list_score.append(0.0)
		        
		self.list_score = list_score
		# print(self.list_score)

		## calculate extra score
		list_score_ext = []
		for time_used in self.list_time_used:
			# get extra score if answer within 60 seconds
		    if time_used<=60:
		        list_score_ext.append(6/time_used)
		    else:
		        list_score_ext.append(0)
		self.list_score_ext = list_score_ext
		# print(self.list_score_ext)

		## combine normal and extra scores
		list_score_final = []
		for idx, q_score in enumerate(self.list_score):
		    if q_score==1:
		        score_cb = q_score + self.list_score_ext[idx]
		        list_score_final.append(score_cb)
		    else:
		        list_score_final.append(q_score)
		self.list_score_final = list_score_final
		# print(self.list_score_final)

		## calculate quiz score
		self.quiz_score = sum(self.list_score_final)
		# print(self.quiz_score)

		return self.quiz_score




