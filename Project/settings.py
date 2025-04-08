import flask
import flask_migrate
import flask_sqlalchemy
import os

#Створення змінної project
project = flask.Flask(
   import_name = "Project",
   static_url_path = "/static/",
   static_folder = "static",
   template_folder = "templates",
   instance_path = os.path.abspath(os.path.join(__name__, ".."))
)

# Налаштування шляху до бази даних (SQLite), яку буде використовувати SQLAlchemy
project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

"""
Команди для роботи з міграціями бази даних у консолі:

1. Ініціалізація міграцій (створює папку migrations)
   flask --app project db init

2. Створення нової міграції на основі змін у моделях
   flask --app project db migrate

3. Застосування міграцій до бази даних (оновлення структури)
   flask --app project db upgrade
"""

# Ініціалізація об'єкта бази даних (SQLAlchemy) з підключенням до Flask-додатку
DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)

# Підключення системи міграцій (Flask-Migrate) до додатку та бази даних
migrate = flask_migrate.Migrate(app = project, db = DATABASE)