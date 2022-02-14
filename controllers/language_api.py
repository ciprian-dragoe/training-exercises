from flask import Blueprint, request, jsonify
import services.language_execution_factory as language_execution_factory
import services.language_reader_factory as language_reader_factory


languages_route = Blueprint('api/language/', __name__)


@languages_route.route("/<language_type>/execute", methods=["POST"])
def execute_language(language_type):
    factory = language_execution_factory.manufacture(language_type)
    result = factory(request.json["code"], request.json["user"], request.json["exerciseNumber"])

    return jsonify(result)


@languages_route.route("/<language_type>/read/<user>/<exercise_number>")
def get_language(user, exercise_number, language_type):
    try:
        factory = language_reader_factory.manufacture(language_type)
        result = factory(user, exercise_number)
        return jsonify({"code": result})
    except Exception as e:
        return jsonify(e.args[0]), 203
