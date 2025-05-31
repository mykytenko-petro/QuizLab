import os
import dotenv

def assemble():
    # node modules 
    os.system("npm install typescript --save-dev")
    os.system("npm i --save-dev @types/jquery")

    # typescript building
    os.system("npx tsc --build .")

    # dotenv
    DOTENV_PATH = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))

    if os.path.exists(path= DOTENV_PATH):
        dotenv.load_dotenv(dotenv_path= DOTENV_PATH)

    # database
    MIGRATIONS_PATH = os.path.abspath(os.path.join(__file__, '..', "migrations"))

    if not os.path.exists(path= MIGRATIONS_PATH):
        os.system("flask --app Project db init")
    
    os.system("flask --app Project db migrate")
    os.system("flask --app Project db upgrade")