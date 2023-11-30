import json
from quizutils.quiz import Quiz, QuestionMC, QuestionTF, Answer

class JSONQuizParser:
    def __init__(self):
        pass

    def import_data(self, quizpath):
        with open(quizpath, 'r') as quizfile:
            quiz_data = json.load(quizfile)

        return quiz_data


    def parse_quiz(self, quizpath):
        quiz_data = self.import_data(quizpath)

        new_quiz = Quiz()
        new_quiz.name = quiz_data['quizname']
        new_quiz.description = quiz_data['description']

        for q_data in quiz_data['questions']:
            if q_data['type'] == 'tf':
                question = QuestionTF()
            elif q_data['type'] == 'mc':
                question = QuestionMC()

            question.text = q_data['text']
            question.correct_answer = q_data['answer']
            question.points = int(q_data['points'])
            new_quiz.total_points += question.points

            for a_data in q_data['choices']:
                answer = Answer()
                answer.name = a_data
                answer.text = q_data['choices'][a_data]
                question.answers.append(answer)

            new_quiz.questions.append(question)

        return new_quiz

