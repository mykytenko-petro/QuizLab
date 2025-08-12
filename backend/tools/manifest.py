import os

import dotenv

def load_env():
    DOTENV_PATH = os.path.abspath(os.path.join(__file__, "..", "..", "..", ".env"))

    if os.path.exists(DOTENV_PATH):
        dotenv.load_dotenv(DOTENV_PATH)

def assemble():
    # media
    for media_folder in ["images", "audio"]:
        os.makedirs(
            os.path.abspath(os.path.join(
                __file__, "..", "..", "Project", "media", media_folder
            )),
            exist_ok=True
        )

    # frontend
    os.chdir(os.path.abspath(os.path.join(__file__, "..", "..", "..", "frontend")))

    os.system("npm install")
    os.system("npx vite build")

    os.chdir(os.path.abspath(os.path.join(__file__, "..", "..")))

    # dotenv
    load_env()