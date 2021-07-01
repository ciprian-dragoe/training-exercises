from flask import Flask, render_template, request, jsonify
from file_generator import get_max_number_exercises, create_user_files
from dotenv import load_dotenv
from storage.database import execute_select


app = Flask('dom-manipulation')
load_dotenv()


@app.route('/')
@app.route('/exercises')
@app.route('/exercises/')
def get_index():
    max_number_exercises = get_max_number_exercises()
    return render_template("index.html", max_number_exercises=max_number_exercises)


@app.route('/exercises/<exercise_number>/<file_name>')
def getExercise(exercise_number, file_name):
    try:
        create_user_files(file_name, exercise_number)
        return render_template(f"{file_name}-{exercise_number}.html", file_name=file_name, exercise_number=exercise_number)
    except:
        return f"Could not create template with name : <h1>{file_name}</h1>"


@app.route('/sql/execute', methods=["POST"])
def run_sql():
    try:
        query_result = execute_select(request.json["query"])
        return jsonify(query_result)
    except Exception as e:
        return f"Could not run sql code"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
