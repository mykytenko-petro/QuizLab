import home_app
import create_quiz_app
from .settings import project

project.register_blueprint(home_app.homeApp)
project.register_blueprint(create_quiz_app.createQuizApp)