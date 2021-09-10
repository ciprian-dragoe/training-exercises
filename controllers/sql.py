from flask import Blueprint, request, jsonify
from services import exercises


sql_route = Blueprint('sql', __name__)


@sql_route.route("/execute", methods=["POST"])
def run_sql():
    try:
        if request.json.get("user") and request.json.get("exerciseNumber"):
            exercises.write_sql_query(
                request.json["user"],
                request.json["exerciseNumber"],
                request.json["query"],
            )

        query_result = exercises.execute_select(request.json["query"])
        return jsonify(query_result)
    except Exception as e:
        return jsonify(e.args[0]), 203


@sql_route.route("/<user>/<exercise_number>")
def get_sql(user, exercise_number):
    try:
        file_path = exercises.get_file_path("*.sql", user, exercise_number)
        with open(file_path, "r") as file:
            return jsonify({"query": file.read()})
    except Exception as e:
        return jsonify(e.args[0]), 203
