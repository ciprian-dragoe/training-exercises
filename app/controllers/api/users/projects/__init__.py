from services import projects
from controllers.api.users.projects.files import api_files


from flask import Blueprint, jsonify, request


api_projects = Blueprint('api/user/<int:user_id>/projects/', __name__)
api_projects.register_blueprint(api_files, url_prefix='/<int:project_id>/files')


@api_projects.route("/<int:project_id>")
def get_project(user_id, project_id):
    result = projects.get(user_id, project_id)
    return jsonify({"project": result})


@api_projects.route("/", methods = ["Post"])
def create_project(user_id):
    project = projects.create_from_starter_template(user_id, request.json['starterProjectId'])
    return jsonify({"project": project})
