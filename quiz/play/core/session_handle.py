from ...create.core.question import read_question
from ...create.models import Quiz
# from ..models import QuizSession


# def quiz_session_handle(id : int, question_index : int):
#     quiz_session: QuizSession = QuizSession.query.filter_by(id=id).first()
#     quiz: Quiz = Quiz.query.filter_by(id=quiz_session.quiz_id)

#     return read_question(question=quiz.questions[question_index])