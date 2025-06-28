import flask
import flask_login
import json
from os.path import abspath, join
from Project.db import DATABASE
from .models import Quiz, Question, Answer

def handle_quiz_data():
    print(flask.request.form)
    json_data = json.loads(flask.request.form["data"])
    file_data = flask.request.files

    if "quiz" in json_data:
        if "id" in json_data["quiz"]:
            quiz: Quiz = Quiz.query.filter_by(id= json_data["quiz"]["id"]).first()

            if json_data["goal"] == "edit":
                quiz.name = json_data["quiz"]["name"]
                quiz.description = json_data["quiz"]["description"]

                image = file_data.get('image')
                if image:
                    image.save(dst= abspath(join(__file__, "..", "..", "Project", "static", "media", "images", f"{image.filename}")))
                    quiz.image = image.filename

                DATABASE.session.add(quiz)
                DATABASE.session.commit()

                return quiz.to_dict()

            elif json_data["goal"] == "delete":
                DATABASE.session.delete(quiz)
                DATABASE.session.commit()

                return {}
            
            elif json_data["goal"] == "get":
                data_dict = {}

                data_dict["quiz"] = quiz.to_dict()
                data_dict["questions"] = []

                for question in quiz.questions:
                    data_dict["questions"].append(question.to_dict())

                return data_dict
                
        else:
            quiz = Quiz()

            quiz.name = "your quiz"
            quiz.description = ""
            quiz.image = "default.png"

            flask_login.current_user.quizzes.append(quiz)
            DATABASE.session.commit()

            return { "id": quiz.id }
        
    elif "question" in json_data:
        if "id" in json_data["question"]:
            question: Question = Question.query.filter_by(id= json_data["question"]["id"]).first()

            if json_data["goal"] == "edit":
                question.description = json_data["question"]["description"]

                image = file_data.get('image')
                if image:
                    image.save(dst= abspath(join(__file__, "..", "..", "Project", "static", "media", "images", f"{image.filename}")))
                    question.image = image.filename

                DATABASE.session.add(question)
                DATABASE.session.commit()
            
            elif json_data["goal"] == "get":
                data_dict = {}
                
                data_dict["question"] = question.to_dict()
                data_dict["answers"] = []


                for answer in question.answers:
                    data_dict["answers"].append(answer.to_dict())

                return data_dict


            elif json_data["goal"] == "delete":
                DATABASE.session.delete(question)
                DATABASE.session.commit()

                return {}
                
            return question.to_dict()

        else:
            quiz = Quiz.query.filter_by(id= json_data["quiz_id"]).first()
            question = Question()

            question.description = "your question"
            question.image = "default.png"

            quiz.questions.append(question)
            DATABASE.session.add(quiz)
            DATABASE.session.commit()

            return { "id": question.id }
        
    elif "answer" in json_data:
        if "id" in json_data["answer"]:
            answer: Answer = Answer.query.filter_by(id= json_data["answer"]["id"]).first()

            if json_data["goal"] == "edit":
                answer.description = json_data["answer"]["description"]

                image = file_data.get('image')
                if image:
                    image.save(dst= abspath(join(__file__, "..", "..", "Project", "static", "media", "images", f"{image.filename}")))
                    answer.image = image.filename
                
                answer.is_right = json_data["answer"]["is_right"] 

                DATABASE.session.add(answer)
                DATABASE.session.commit()

                return answer.to_dict()
            
            elif json_data["goal"] == "delete":
                DATABASE.session.delete(answer)
                DATABASE.session.commit()

                return {}
            
            elif json_data["goal"] == "get":
                return answer.to_dict()
        
        else:
            question = Question.query.filter_by(id= json_data["question_id"]).first()
            answer = Answer()
            
            answer.description = "your answer"
            answer.image = "default.png"

            question.answers.append(answer)
            DATABASE.session.add(question)
            DATABASE.session.commit()

            return { "id": answer.id }