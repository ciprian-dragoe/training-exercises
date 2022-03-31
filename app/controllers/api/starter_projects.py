from services import files


from flask import Blueprint, jsonify


api_languages = Blueprint('api/files/', __name__)


@api_languages.route("/users/<int:user_id>/files/<int:file_id>")
def get_language(user_id, file_id):
    result = files.get(file_id, user_id)
    return jsonify({"content": result})


# todo: split this route in users / files
