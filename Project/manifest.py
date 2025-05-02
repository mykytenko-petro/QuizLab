import os
import dotenv

DOTENV_PATH = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
MIGRATIONS_PATH = os.path.abspath(os.path.join(__file__, '..', "migrations"))

def assemble():
    if os.path.exists(path= DOTENV_PATH):
        dotenv.load_dotenv(dotenv_path= DOTENV_PATH)

    if not os.path.exists(path= MIGRATIONS_PATH):
        os.system(os.environ["DB_INIT"])
    
    os.system(os.environ["DB_MIGRATE"])
    os.system(os.environ["DB_UPGRADE"])