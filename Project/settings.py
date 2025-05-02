import flask
import flask_migrate
import flask_sqlalchemy
import os


# Create Flask app
project = flask.Flask(
   import_name="Project",
   static_url_path="/static",
   static_folder="static",
   template_folder="templates",
   instance_path=os.path.abspath(os.path.join(__file__, "..", "instance"))
)

# Configure database
project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app= project)

# Initialize the database with our app
project.app_context().push()

# Set up migrations
migrate = flask_migrate.Migrate(
   app=project,
   db=DATABASE,
   directory=os.path.abspath(os.path.join(__file__, "..", "migrations"))
)