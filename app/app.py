from flask import Flask, redirect


from services import app_configuration
from controllers.display.admin import display_admin
from controllers.display.users import *
from controllers.display.starter_projects import display_starter_projects
from controllers.api.admin import api_admin
from controllers.api.users import *
from controllers.api.languages import api_languages
from controllers.api.starter_projects import api_starter_projects
from data.configuration import CONFIGURATION


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/starter-projects/")


def initialize_app():
    app_configuration.initialize(app)
    app.register_blueprint(display_admin, url_prefix='/admin/')
    app.register_blueprint(api_admin, url_prefix='/api/admin/')

    app.register_blueprint(display_users, url_prefix='/users/')

    app.register_blueprint(display_starter_projects, url_prefix='/starter-projects/')
    app.register_blueprint(api_starter_projects, url_prefix='/api/starter-projects/')

    app.register_blueprint(api_users, url_prefix='/api/users/')

    app.register_blueprint(api_languages, url_prefix='/api/language/')


initialize_app()


if __name__ == "__main__":
    app.run(debug=CONFIGURATION["FLASK_ENV"] == "development", port=80, host='0.0.0.0')
