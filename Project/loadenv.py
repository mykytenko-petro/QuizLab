import dotenv
import os

PATH = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
if os.path.exists(path= PATH):
    dotenv.load_dotenv(PATH)

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
