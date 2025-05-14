import flask
import os

# Create Flask app
project = flask.Flask(
   import_name="Project",
   static_url_path="/static",
   static_folder="static",
   template_folder="templates",
   instance_path=os.path.abspath(os.path.join(__file__, "..", "instance"))
)