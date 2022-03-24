import os
from dotenv import load_dotenv
from data.configuration import CONFIGURATION
load_dotenv()


def initialize(app):
    app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
    CONFIGURATION["FLASK_ENV"] = os.environ.get("FLASK_ENV")
    CONFIGURATION["PRACTICE_DBNAME"] = os.environ.get("PRACTICE_DBNAME")
    CONFIGURATION["PRACTICE_USER"] = os.environ.get("PRACTICE_USER")
    CONFIGURATION["PRACTICE_HOST"] = os.environ.get("PRACTICE_HOST")
    CONFIGURATION["PRACTICE_PORT"] = os.environ.get("PRACTICE_PORT")
    CONFIGURATION["PRACTICE_PASS"] = os.environ.get("PRACTICE_PASS")
    CONFIGURATION["ADMIN_DASHBOARD_PASS"] = os.environ.get("ADMIN_DASHBOARD_PASS")
    CONFIGURATION["DOCKER_KILL_TIMEOUT_SECONDS"] = os.environ.get("DOCKER_KILL_TIMEOUT_SECONDS")

