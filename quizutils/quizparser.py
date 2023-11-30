import json
from quizutils.quiz import Quiz, QuestionMC, QuestionTF, Answer

class JSONQuizParser:
    def __init__(self):
        pass

    def import_data(self, quizpath):
        with open(quizpath, 'r') as quizfile:
            quiz_data = json.load(quizfile)

        return quiz_data


    def create_question_obj(self, data):
        if data['type'] == 'tf':
            question_obj = QuestionTF()

        elif data['type'] == 'mc':
            question_obj = QuestionMC()

            # add answer object to question object
            for a_data in data['choices']:
                answer = Answer()
                answer.name = a_data
                answer.text = data['choices'][a_data]
                question_obj.answers.append(answer)

        return question_obj


    def parse_quiz(self, quizpath):
        quiz_data = self.import_data(quizpath)

        new_quiz = Quiz()
        new_quiz.name = quiz_data['quizname']
        new_quiz.description = quiz_data['description']

        for q_data in quiz_data['questions']:

            question = self.create_question_obj(q_data)
            question.text = q_data['text']
            question.correct_answer = q_data['answer']
            question.points = int(q_data['points'])
            new_quiz.total_points += question.points
            new_quiz.questions.append(question)

        return new_quiz

