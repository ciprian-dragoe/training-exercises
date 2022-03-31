from services.languages import languages


from flask import Blueprint, request, jsonify


api_languages = Blueprint('api/language/', __name__)


@api_languages.route("/<language_type>/execute", methods=["POST"])
def execute_language(language_type):
    result = languages.process(language_type, request.json["code"], request.json["user_id"], request.json["file_id"])
    return jsonify(result)
