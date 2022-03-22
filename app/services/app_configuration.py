import os
from dotenv import load_dotenv
from data.configuration import CONFIGURATION
load_dotenv()


def initialize(app):
    CONFIGURATION["RUNNING-MODE"] = os.environ.get("RUNNING_MODE")
    CONFIGURATION["DOCKER-IMAGE-NAME"] = os.environ.get("DOCKER_IMAGE_NAME")
    CONFIGURATION["MY_PSQL_DBNAME"] = os.environ.get("MY_PSQL_DBNAME")
    CONFIGURATION["MY_PSQL_USER"] = os.environ.get("MY_PSQL_USER")
    CONFIGURATION["MY_PSQL_HOST"] = os.environ.get("MY_PSQL_HOST")
    CONFIGURATION["MY_PSQL_PASSWORD"] = os.environ.get("MY_PSQL_PASSWORD")
    CONFIGURATION["DOCKER-KILL-TIMEOUT-SECONDS"] = os.environ.get("DOCKER-KILL-TIMEOUT-SECONDS")

