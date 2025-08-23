import os

import dotenv

def loadenv():
    DOTENV_PATH = os.path.abspath(os.path.join(__file__, "..", ".env"))

    if os.path.exists(path=DOTENV_PATH):
        dotenv.load_dotenv(dotenv_path=DOTENV_PATH)

        print("succsesfully loaded .env")
    else:
        print(".env not found on this path:" + DOTENV_PATH)

def assemble():
    # media
    for folder in ["images", "sounds"]:
        os.makedirs(
            os.path.abspath(os.path.join(
                __file__, "..", "Project", "media", folder
            )),
            exist_ok=True
        )

    # node modules 
    os.system("npm install")

    # typescript compiling
    os.system("npm run build")

    # dotenv
    loadenv()
    
    # database
    MIGRATIONS_PATH = os.path.abspath(os.path.join(__file__, '..', "Project", "migrations"))

    if not os.path.exists(path=MIGRATIONS_PATH):
        os.system("flask --app Project db init")
    
    os.system("flask --app Project db migrate")
    os.system("flask --app Project db upgrade")