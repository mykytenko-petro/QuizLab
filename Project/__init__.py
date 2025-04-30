from .manifest import assemble
from .urls import *
from .settings import project
from .login_manager import *

project.register_blueprint(home_app.homeApp)
project.register_blueprint(registration_app.registrationApp)
project.register_blueprint(registration_app.loginApp)