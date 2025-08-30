import flask

from Project.utils import page_config
from ..models import User


@page_config(template_name="profile.html")
def render_profile(id : int):
    user = User.query.filter_by(id=id).first()
    
    return {"profile" : user}