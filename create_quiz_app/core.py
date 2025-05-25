import flask
import flask_login
from Project.db import DATABASE
from .models import Quiz, Question, Answer

class AssembleQuiz:
    @staticmethod
    def handle_data(data):
        if "quiz" in data:
            return AssembleQuiz.create_quiz(data)

        elif "question" in data:
            return AssembleQuiz.create_question(data)

        elif "question" in data:
            return AssembleQuiz.create_answer(data)

    @staticmethod
    def create_quiz(data):
        match data["goal"]:
            case "create":
                quiz = Quiz()
                print("objects", dir(quiz))

                flask_login.current_user.quizzes.append(quiz)
                DATABASE.session.commit()

                return flask.redirect("/")

            case "edit":
                quiz: Quiz = Quiz.query.filter_by(id= data["quiz"]["quiz_id"]).first()

                quiz.name = data["name"]
                quiz.description = data["description"]

                DATABASE.session.add(quiz)
                DATABASE.session.commit()

            case "delete":
                quiz: Quiz = Quiz.query.filter_by(id= data["quiz_id"]).first()

                DATABASE.session.delete(quiz)
                DATABASE.session.commit()

                return {}

        return quiz.to_dict()

    @staticmethod
    def create_question(data):
        match data["goal"]:
            case "create":
                quiz = Quiz.query.filter_by(id= data["quiz_id"]).first()
                question = Question()

                quiz.questions.append(question)

                DATABASE.session.add(quiz)
                DATABASE.session.commit()

            case "edit":
                question: Question = Question.query.filter_by(id= data["quiz_id"]).first()

                question.description = data["description"]
                question.path_to_image = data["path_to_image"]

                DATABASE.session.add(question)
                DATABASE.session.commit()

            case "delete":
                question: Question = Question.query.filter_by(id= data["quiz_id"]).first()

                DATABASE.session.delete(question)
                DATABASE.session.commit()

                return {}

        return question.to_dict()

    @staticmethod
    def create_answer(data):
        match data["goal"]:
            case "create":
                question = Question.query.filter_by(id= data["quiz_id"]).first()
                answer = Answer()

                question.answers.append(answer)

                DATABASE.session.add(question)
                DATABASE.session.commit()

            case "edit":
                answer: Answer = Answer.query.filter_by(id= data["quiz_id"]).first()

                answer.description = data["description"]
                answer.path_to_image = data["path_to_image"]

                DATABASE.session.add(question)
                DATABASE.session.commit()

            case "delete":
                answer: Answer = Answer.query.filter_by(id= data["quiz_id"]).first()

                DATABASE.session.delete(answer)
                DATABASE.session.commit()

                return {}

        return answer.to_dict()