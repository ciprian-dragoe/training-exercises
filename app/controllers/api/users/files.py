from services import files


from flask import Blueprint, jsonify


api_files = Blueprint('api/user/<int:user_id>/files/', __name__)


@api_files.route("/<int:file_id>")
def get_language(user_id, file_id):
    result = files.get(file_id, user_id)
    return jsonify({"file": result})
