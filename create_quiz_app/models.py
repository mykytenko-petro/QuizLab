from Project.db import BaseModel, DATABASE as DB

class Quiz(BaseModel):
    id = DB.Column(DB.Integer, primary_key = True)
    owner_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable = False)

    name = DB.Column(DB.String(50), nullable = True)
    description = DB.Column(DB.String(256), nullable = True)

    questions = DB.relationship('Question', backref = 'quiz', cascade='all, delete-orphan')

class Question(BaseModel):
    id = DB.Column(DB.Integer, primary_key = True)
    quiz_id = DB.Column(DB.Integer, DB.ForeignKey('quiz.id'), nullable = False)

    description = DB.Column(DB.String(256), nullable = True)
    path_to_image = DB.Column(DB.String(256), nullable = True)
    
    answers = DB.relationship('Answer', backref = 'question', cascade='all, delete-orphan')

class Answer(BaseModel):
    id = DB.Column(DB.Integer, primary_key = True)
    question_id = DB.Column(DB.Integer, DB.ForeignKey('question.id'), nullable = False)

    description = DB.Column(DB.String(256), nullable = True)
    path_to_image = DB.Column(DB.String(256), nullable = True)
    is_right = DB.Column(DB.Boolean, default = False, nullable = True)