class Questions:
	def __init__(self, question_info):
		self.question = question_info['text']
		self.type = question_info['type']
		self.points = question_info['points']
		self.answer = question_info['answer']



class MCQuestion(Questions):
	def __init__(self, question_info):
		Questions.__init__(self, question_info)
		self.choices = question_info['choices']



class TFQuestion(Questions):
	def __init__(self, question_info):
		Questions.__init__(self, question_info)
		self.choices = ['True', 'False']


