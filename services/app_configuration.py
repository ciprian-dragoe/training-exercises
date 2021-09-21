import os
import bcrypt
from dotenv import load_dotenv
from data.configuration import CONFIGURATION
load_dotenv()


def initialize(flask_app):
    flask_app.secret_key = os.environ.get("APP_SECRET_KEY")
    CONFIGURATION["ADMIN-HASHED-PASSWORD"] = bcrypt.hashpw(os.environ.get("ADMIN_DASHBOARD_PASS").encode(), bcrypt.gensalt())
    CONFIGURATION["DOCKER-IMAGE-NAME"] = os.environ.get("DOCKER_IMAGE_NAME")
    CONFIGURATION["MY_PSQL_DBNAME"] = os.environ.get("MY_PSQL_DBNAME")
    CONFIGURATION["MY_PSQL_USER"] = os.environ.get("MY_PSQL_USER")
    CONFIGURATION["MY_PSQL_HOST"] = os.environ.get("MY_PSQL_HOST")
    CONFIGURATION["MY_PSQL_PASSWORD"] = os.environ.get("MY_PSQL_PASSWORD")
    CONFIGURATION["DOCKER-KILL-TIMEOUT-SECONDS"] = os.environ.get("DOCKER-KILL-TIMEOUT-SECONDS")

