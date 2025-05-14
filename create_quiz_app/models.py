from Project.settings import DATABASE

class Quiz(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    owner = ...

    name = DATABASE.Column(DATABASE.String(50), nullable = False)
    description = DATABASE.Column(DATABASE.String(256), nullable = True)

    questions = ...

class Question(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    quiz = ...

    description = DATABASE.Column(DATABASE.String(256), nullable = False)
    path_to_image = DATABASE.Column(DATABASE.String(256), nullable = True)
    multiple_answers = DATABASE.Column(DATABASE.Boolean, default = False, nullable = False)
    
    answers = ...

class Answer(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    question = ...

    description = DATABASE.Column(DATABASE.String(256), nullable = False)
    is_right = DATABASE.Column(DATABASE.Boolean, default = False, nullable = False)
    path_to_image = DATABASE.Column(DATABASE.String(256), nullable = True)