import flask_session
import datetime
from .settings import project
from .db import DATABASE

project.config["SESSION_TYPE"] = "sqlalchemy"
project.config["SESSION_SQLALCHEMY"] = DATABASE
project.config["SESSION_PERMANENT"] = True
project.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(weeks= 2)

flask_session.Session(app= project)