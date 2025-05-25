import flask_migrate
import flask_sqlalchemy
import sqlalchemy
import os
from .settings import project

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
project.app_context().push()

DATABASE: sqlalchemy = flask_sqlalchemy.SQLAlchemy(app= project)

class BaseModel(DATABASE.Model):
    r"""
        custom model with useful methods
    """

    __abstract__ = True
    
    def to_dict(self):
        r"""
            returns model representation as a dict
            (relationships are not supported)
        """

        model_dict = {}

        for column in self.__table__.columns:
            model_dict.update({column.name: getattr(self, column.name)})

        return model_dict

migrate = flask_migrate.Migrate(
    app=project,
    db=DATABASE,
    directory=os.path.abspath(os.path.join(__file__, "..", "migrations"))
)