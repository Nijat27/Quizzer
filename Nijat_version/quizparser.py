import json
from quiz import Quiz, QuestionMC, QuestionTF, Answer

class JSONQuizParser:
    def __init__(self):
        pass

    def parse_quiz(self, quizpath):
        with open(quizpath, 'r') as quizfile:
            quiz_data = json.load(quizfile)['Quiz']

        new_quiz = Quiz()
        new_quiz.name = quiz_data['name']
        new_quiz.description = quiz_data['Description']

        for q_data in quiz_data['Questions']:
            if q_data['type'] == 'tf':
                question = QuestionTF()
            elif q_data['type'] == 'mc':
                question = QuestionMC()

            question.text = q_data['QuestionText']['text']
            question.correct_answer = q_data['QuestionText']['answer']
            question.points = int(q_data['points'])
            new_quiz.total_points += question.points

            for a_data in q_data.get('Answers', []):
                answer = Answer()
                answer.name = a_data['name']
                answer.text = a_data['text']
                question.answers.append(answer)

            new_quiz.questions.append(question)

        return new_quiz
