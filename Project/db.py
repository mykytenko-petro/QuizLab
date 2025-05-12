import os
import flask_sqlalchemy
import flask_migrate
from .settings import project

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app= project)

project.app_context().push()

migrate = flask_migrate.Migrate(
   app= project,
   db= DATABASE,
   directory= os.path.abspath(os.path.join(__file__, "..", "migrations"))
)