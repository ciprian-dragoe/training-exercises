import atexit
from flask import Flask, redirect
from services import app_configuration
from controllers.admin import admin_route
from controllers.sql import sql_route
from controllers.exercises import exercises_route
from services.docker import kill_existing_containers


app = Flask("exercises")


@app.route("/")
def index():
    return redirect("/exercises/")


def initialize_app():
    app_configuration.initialize(app)
    app.register_blueprint(admin_route, url_prefix='/admin')
    app.register_blueprint(sql_route, url_prefix='/api/sql')
    app.register_blueprint(exercises_route, url_prefix='/exercises')


def de_initialize_app():
    kill_existing_containers()


atexit.register(de_initialize_app)
if __name__ == "__main__":
    initialize_app()
    app.run(debug=True)
