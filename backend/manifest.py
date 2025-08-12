import os

import dotenv


def assemble():
    # media
    for media_folder in ["images", "audio"]:
        os.makedirs(
            os.path.abspath(os.path.join(
                "Project", "media", media_folder
            )),
            exist_ok=True
        )

    # frontend
    os.chdir(os.path.abspath(os.path.join(__file__, "..", "..", "frontend")))

    os.system("npm install")
    os.system("npx vite build")

    os.chdir(os.path.abspath(os.path.join(__file__, "..")))

    # dotenv
    DOTENV_PATH = os.path.abspath(os.path.join(".env"))

    if os.path.exists(DOTENV_PATH):
        dotenv.load_dotenv(DOTENV_PATH)

    # database
    os.system('alembic revision --autogenerate -m ""')
    os.system('alembic upgrade head')