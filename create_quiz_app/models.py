from Project.db import DATABASE as DB

class Quiz(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    owner = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable = False)

    name = DB.Column(DB.String(50), nullable = False)
    description = DB.Column(DB.String(256), nullable = True)

    questions = DB.relationship('Question', backref = 'user', cascade='all, delete-orphan')

class Question(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    quiz = DB.Column(DB.Integer, DB.ForeignKey('quiz.id'), nullable = False)

    description = DB.Column(DB.String(256), nullable = False)
    path_to_image = DB.Column(DB.String(256), nullable = False)
    
    answers = DB.relationship('Answer', backref = 'user', cascade='all, delete-orphan')

class Answer(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    question = DB.Column(DB.Integer, DB.ForeignKey('question.id'), nullable = False)

    description = DB.Column(DB.String(256), nullable = False)
    path_to_image = DB.Column(DB.String(256), nullable = True)
    is_right = DB.Column(DB.Boolean, default = False, nullable = False)