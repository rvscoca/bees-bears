import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "please_change_me")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
