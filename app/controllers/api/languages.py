from services.languages import languages


from flask import Blueprint, request, jsonify


api_languages = Blueprint('api/language/', __name__)


@api_languages.route("/<language_type>/update-file-and-run-code", methods=["POST"])
def execute_language(language_type):
    result = languages.process(language_type, request.json["code"], request.json["userId"], request.json["fileId"])
    return jsonify(result)


@api_languages.route("/<language_type>/run-code", methods=["POST"])
def execute_language(language_type):
    result = languages.process(language_type, request.json["code"])
    return jsonify(result)
