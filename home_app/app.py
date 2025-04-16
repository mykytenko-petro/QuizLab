import flask

#Створеня застосунку homeApp.
homeApp = flask.Blueprint(
    name = "home", #Назва додатку
    import_name = "home_app", #Папка, в якій знаходиться наш додаток
    template_folder = "templates",#Папка, де зберігаються шаблони
    static_url_path = "/home_app/static",#Шлях до папки static
    static_folder = "static",#Означає, як називаеться статична папка
)