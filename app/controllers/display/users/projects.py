from services import projects


from flask import Blueprint, render_template_string


display_projects = Blueprint('/users/<int:user_id>/projects', __name__)


@display_projects.route("/<int:project_id>")
def render_projects(user_id, project_id):
    template_content, template_name = projects.get_project_starter_template(user_id, project_id)
    return render_template_string(template_content, template=template_name)
