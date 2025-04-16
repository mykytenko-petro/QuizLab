import flask

#Додаток авторизації
authorizationApp = flask.Blueprint(
    name = "login",#Ім'я нашого додатку
    import_name = "login_app",#Місце, де знаходиться  login_app
    template_folder = "login_page/templates",#Шлях до папки, де зберігаються шаблони
    static_url_path = "/login/",#Шлях до папки static
    static_folder = "login_page/static",#Назва статичної папки
)

