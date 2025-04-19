import dotenv
import os

PATH = os.path.abspath(os.path.join(__file__, "..", ".env"))
dotenv.load_dotenv(PATH)

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")