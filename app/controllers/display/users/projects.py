from flask import Blueprint, render_template
from services import projects


display_projects = Blueprint('/users/<int:user_id>/projects', __name__)


@display_projects.route("/<int:project_id>")
def render_projects(user_id, project_id):
    template_name = projects.get(user_id, project_id)['name']
    return render_template(f"starter-projects/{template_name}/index.html")
