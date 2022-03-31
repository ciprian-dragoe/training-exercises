from flask import Blueprint, render_template


display_starter_projects = Blueprint('starter-projects', __name__)


@display_starter_projects.route("/")
def render_exercises():
    return render_template("starter-projects.html")
