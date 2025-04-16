import home_app
import create_quiz_app
import login_app
import registration_app
from .settings import project

project.register_blueprint(home_app.homeApp)#У цій строі знаходиться шлях до додатку home_app
project.register_blueprint(create_quiz_app.createQuizApp)#У цій строі знаходиться шлях до додатку createQuizapp
project.register_blueprint(login_app.authorizationApp)#У цій строі знаходиться шлях до додатку authorizationApp
# project.register_blueprint(registration_app.registrationApp)