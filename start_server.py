from flask import Flask, render_template, url_for, request, redirect
from file_generator import get_max_number_exercises, create_user_files


app = Flask('dom-manipulation')


@app.route('/')
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


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
