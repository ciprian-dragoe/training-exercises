from flask import Blueprint, render_template
from services import starter_projects


exercises_route = Blueprint('starter-projects', __name__)


@exercises_route.route("/")
def display_exercises():
    return render_template("starter-projects.html")


@exercises_route.route("/<exercise_number>/<file_name>")
def display_exercise(exercise_number, file_name):
    exercises.create_user_files(file_name, exercise_number)
    return render_template(
        f"exercises/{file_name}-{exercise_number}-index.html",
        file_name=file_name,
        exercise_number=exercise_number,
    )
