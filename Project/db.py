import os

import flask_migrate
import flask_sqlalchemy
import sqlalchemy

from .settings import project


project.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_URL"]
project.app_context().push()

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = sqlalchemy.MetaData(naming_convention=convention)
DATABASE = flask_sqlalchemy.SQLAlchemy(app=project, metadata=metadata)

migrate = flask_migrate.Migrate(
    app=project,
    db=DATABASE,
    directory=os.path.abspath(os.path.join(__file__, "..", "migrations"))
)