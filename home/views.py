from Project.utils import page_config


@page_config("home.html")
def render_home():
    return None

@page_config("home.html")
def render_dashboard():
    
    return {"quizes": ...}