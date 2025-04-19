###import flask_login
###import registration_app
###from registration_app.models import User
###from flask_login import LoginManager

import flask_login
from .settings import project

login_manager = flask_login.LoginManager(app=project)

@login_manager.user_loader
def load_user(id):
    # Delay import until function call to avoid circular imports
    from registration_app.models import User
    return User.query.get(int(id))
##import flask_login
##from .settings import project
##from registration_app.models import User
##
##project.secret_key = "SECRET_KEY123"
##login_manager = flask_login.LoginManager(app = project)
##
##@login_manager.user_loader
##def load_user(id):
##    return User.query.get(id)


#registration_app.secret_key = "SECRET_KEY123"
#login_manager = LoginManager(app = registration_app.registrationApp)
#
#@login_manager.user_loader
#def load_user(id):
#    return User.query.get(id)


###@registration_app.after_request
###def after_request_func(response):
###    print("after_request is running!")
###    return response
###
###app = registration_app
###app.secret_key = 'xxxxyyyyyzzzzz'
###
###login_manager = LoginManager()
###login_manager.init_app(app)
###login_manager.login_view = 'login'

