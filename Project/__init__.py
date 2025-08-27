from . import (
    login_manager,
    session_config
)
from .settings import project
from .media_setup import mediaManagerApp
from .typescript_setup import typescriptManagerApp


project.register_blueprint(blueprint=mediaManagerApp)
project.register_blueprint(blueprint=typescriptManagerApp)

import user
import home
import quiz

project.register_blueprint(blueprint=home.homeApp)
project.register_blueprint(blueprint=user.userApp)
project.register_blueprint(blueprint=quiz.quizApp)