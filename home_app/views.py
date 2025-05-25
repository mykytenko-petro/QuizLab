from Project.utils import toggle, page_config

@toggle(name_of_bp="homeApp")
@page_config(template_name= "home.html")
def render_home():
    return None