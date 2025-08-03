from .manifest import assemble
from .urls import *
from .settings import project
from .login_manager import *
from .session_config import *
from .media_setup import mediaManagerApp
from .typescript_setup import typescriptManagerApp

import api

project.register_blueprint(mediaManagerApp)
project.register_blueprint(typescriptManagerApp)

project.register_blueprint(home.homeApp)
project.register_blueprint(user.registrationApp)
project.register_blueprint(user.loginApp)
project.register_blueprint(api.apiApp)
project.register_blueprint(quiz.createQuizApp)