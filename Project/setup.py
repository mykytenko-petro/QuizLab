import home_app
import create_quiz_app
import login_app
import registration_app
from .settings import project

project.register_blueprint(home_app.homeApp)
project.register_blueprint(create_quiz_app.createQuizApp)
# project.register_blueprint(login_app.authorizationApp)
# project.register_blueprint(registration_app.registrationApp)