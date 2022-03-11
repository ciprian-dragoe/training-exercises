import atexit
from flask import Flask, redirect


from services import app_configuration
from controllers.admin import admin_route
from controllers.language_api import languages_route
from controllers.exercises import exercises_route
from services.docker import kill_existing_containers


app = Flask("exercises")


@app.route("/")
def index():
    return redirect("/exercises/")


def initialize_app():
    app_configuration.initialize(app)
    app.register_blueprint(admin_route, url_prefix='/admin')
    app.register_blueprint(exercises_route, url_prefix='/exercises')
    app.register_blueprint(languages_route, url_prefix='/api/language')


def de_initialize_app():
    kill_existing_containers()


atexit.register(de_initialize_app)
initialize_app()
if __name__ == "__main__":
    app.run(debug=False)
