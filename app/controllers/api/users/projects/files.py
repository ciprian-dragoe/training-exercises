from services import files


from flask import Blueprint, jsonify


api_files = Blueprint('api/user/<int:user_id>/projects/<int:project_id>/files/', __name__)


@api_files.route("/<int:file_id>")
def get_file(user_id, file_id, project_id):
    result = files.get(user_id, project_id, file_id)
    return jsonify({"file": result})


@api_files.route("/")
def get_files(project_id, user_id):
    results = files.get_files(user_id, project_id)
    return jsonify({"files": results})
