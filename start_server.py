from flask import Flask, render_template, url_for, request, redirect
app = Flask('dom-manipulation')
from os import path, listdir


@app.route('/exercises/<exercise_number>/<file_name>')
def getExercise(exercise_number, file_name):
    try:
        create_user_files(file_name, exercise_number)
        return render_template(f"{file_name}-{exercise_number}.html", file_name=file_name, exercise_number=exercise_number)
    except:
        return f"Could not create template with name : <h1>{file_name}</h1>"


def create_user_files(file_name, exercise_number):
    exercise_file_names = get_exercise_files(exercise_number)
    for template_name in exercise_file_names:
        create_from_template_if_not_exist(template_name, file_name, exercise_number)


def get_exercise_files(exercise_number):
    files = [f'./exercises/{exercise_number}/{file}' for file in listdir(f'./exercises/{exercise_number}/')]
    return files  


def create_from_template_if_not_exist(template, file_name, exercise_number):
    file_path = get_file_path(template, file_name, exercise_number)
    if not path.exists(file_path):
        with open(template, "r") as file:
            content = file.read()
        with open(file_path, "w") as file:
            file.write(content)


def get_file_path(template, file_name, exercise_number):
    extension = template.split(".")[-1]
    if extension == "html":
        return f"templates/{file_name}-{exercise_number}.html"
    if extension == "js":
        return f"static/js/{file_name}-{exercise_number}.js"
    if extension == "css":
        return f"static/style/{file_name}-{exercise_number}.css"


def main():
    app.run()


if __name__ == '__main__':
    main()
