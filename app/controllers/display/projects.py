from flask import Blueprint, render_template
from services import projects


exercises_route = Blueprint('projects', __name__)


@exercises_route.route("/users/<int:user_id>/projects/<int:project_id>")
def display_exercises(user_id, project_id):
    template_name = projects.get(user_id, project_id)['name']
    return render_template(f"{template_name}.html")


# todo: split this route in users / files
