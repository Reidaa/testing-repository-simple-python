import os

from dotenv import load_dotenv

from src.t import EnvModel

load_dotenv(override=True)


# dotenv_path = os.path.join(APP_ROOT, ".env")
# load_dotenv(dotenv_path)


env = EnvModel(
    DEBUG=os.getenv("DEBUG"),
    PORT=os.getenv("PORT"),
    DATA_FILE_PATH=os.getenv("DATA_FILE_PATH", default="data.json"),
    # DATABASE_URL=os.getenv("DATABASE_URL"),
    SECRET_KEY=os.getenv("SECRET_KEY"),
    JWT_ACCESS_TOKEN_EXPIRES=os.getenv("JWT_ACCESS_TOKEN_EXPIRES"),
)
