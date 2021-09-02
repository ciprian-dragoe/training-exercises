from flask import Flask, render_template, request, jsonify, url_for

from managers.file import (
    get_max_number_exercises,
    create_user_files,
    write_sql_query,
    get_file_path,
)
from dotenv import load_dotenv
from managers.database import execute_select


app = Flask("dom-manipulation")
load_dotenv()


@app.route("/")
@app.route("/exercises")
@app.route("/exercises/")
def get_index():
    max_number_exercises = get_max_number_exercises()
    return render_template("index.html", max_number_exercises=max_number_exercises)


@app.route("/exercises/<exercise_number>/<file_name>")
@app.route("/exercises/<exercise_number>/<file_name>/")
def getExercise(exercise_number, file_name):
    create_user_files(file_name, exercise_number)

    stylesheet = url_for("static", filename=f"style/{file_name}-{exercise_number}.css")
    script = url_for("static", filename=f"js/{file_name}-{exercise_number}.js")

    return render_template(
        f"{file_name}-{exercise_number}.html",
        stylesheet=stylesheet,
        script=script,
        file_name=file_name,
        exercise_number=exercise_number,
    )


@app.route("/api/sql/execute", methods=["POST"])
@app.route("/api/sql/execute/", methods=["POST"])
def run_sql():
    try:
        if request.json.get("user") and request.json.get("number"):
            write_sql_query(
                request.json["user"],
                request.json["number"],
                request.json["query"],
            )
        query_result = execute_select(request.json["query"])
        return jsonify(query_result)
    except Exception as e:
        return jsonify(e.args[0]), 203


@app.route("/api/sql/<user>/<exercise_number>", methods=["GET"])
@app.route("/api/sql/<user>/<exercise_number>/", methods=["GET"])
def get_sql(user, exercise_number):
    try:
        file_path = get_file_path("*.sql", user, exercise_number)
        with open(file_path, "r") as file:
            return jsonify({"query": file.read()})

    except Exception as e:
        return jsonify(e.args[0]), 203


if __name__ == "__main__":
    app.run(debug=True)
