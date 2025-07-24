import os
from PIL import Image
import dotenv

def assemble():
    # node modules 
    os.system("npm install")

    # typescript compiling
    os.system("npm run build")

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

    #
    os.makedirs(os.path.join(os.path.join(__file__, "..", "media", "images")), exist_ok=True)
