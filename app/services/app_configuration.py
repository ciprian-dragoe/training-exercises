from data.configuration import CONFIGURATION


import os
from dotenv import load_dotenv


load_dotenv()


def initialize(app):
    app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
    CONFIGURATION["NETWORK_NAME"] = os.environ.get("NETWORK_NAME")
    CONFIGURATION["FLASK_ENV"] = os.environ.get("FLASK_ENV")
    CONFIGURATION["PRACTICE_SERVER_TYPE"] = os.environ.get("ADMIN_SERVER_TYPE")
    CONFIGURATION["PRACTICE_HOST"] = os.environ.get("PRACTICE_HOST")
    CONFIGURATION["PRACTICE_PORT"] = os.environ.get("PRACTICE_PORT")
    CONFIGURATION["PRACTICE_USER"] = os.environ.get("PRACTICE_USER")
    CONFIGURATION["PRACTICE_PASS"] = os.environ.get("PRACTICE_PASS")
    CONFIGURATION["PRACTICE_DBNAME"] = os.environ.get("PRACTICE_DBNAME")
    CONFIGURATION["ADMIN_SERVER_TYPE"] = os.environ.get("ADMIN_SERVER_TYPE")
    CONFIGURATION["ADMIN_HOST"] = os.environ.get("ADMIN_HOST")
    CONFIGURATION["ADMIN_PORT"] = os.environ.get("ADMIN_PORT")
    CONFIGURATION["ADMIN_USER"] = os.environ.get("ADMIN_USER")
    CONFIGURATION["ADMIN_PASS"] = os.environ.get("ADMIN_PASS")
    CONFIGURATION["ADMIN_DBNAME"] = os.environ.get("ADMIN_DBNAME")
    CONFIGURATION["ADMIN_DASHBOARD_PASS"] = os.environ.get("ADMIN_DASHBOARD_PASS")
    CONFIGURATION["DOCKER_KILL_TIMEOUT_SECONDS"] = os.environ.get("DOCKER_KILL_TIMEOUT_SECONDS")

