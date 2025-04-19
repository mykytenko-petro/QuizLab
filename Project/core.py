from .settings import project
import home_app, registration_app

project.register_blueprint(home_app.homeApp)
project.register_blueprint(registration_app.registrationApp)