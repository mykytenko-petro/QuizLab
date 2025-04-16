import home_app
import create_quiz_app
import registration_app
import login_app
#Додаємо правило посилання  у до додатку home_app. У якому прив'язуємо функцію відображення сторінки
home_app.homeApp.add_url_rule(rule = '/', view_func = home_app.render_home)

#Тут також додаємо правило посилання, але до createQuizApp. У якому прив'язуємо функцію відображення сторінки
create_quiz_app.createQuizApp.add_url_rule(rule = '/create_quiz', view_func = create_quiz_app.render_create_quiz)
# registration_app.registrationApp.add_url_rule(rule = '/registration', view_func = registration_app.render_registration)
# login_app.authorizationApp.add_url_rule(rule = '/login', view_func = login_app.render_login)