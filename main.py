from flask import Flask, render_template, url_for, request, redirect
app = Flask('dom-manipulation')
from os import path, listdir


# @app.route('/<template_number>')
# def index(template_number):
#     try:
#         return render_template(f"index{template_number}.html", template_number=template_number)
#     except:
#         return f"The template number you were looking for is not found: <h1>{template_number}</h1>"


@app.route('/exercises/<exercise_number>/<file_name>')
def getExercise(exercise_number, file_name):
    try:
        create_user_files(file_name, exercise_number)
        return render_template(f"{file_name}.html", file_name=file_name)
    except:
        return f"Could not create template with name : <h1>{file_name}</h1>"


def create_user_files(file_name, exercise_number):
    exercise_file_names = get_exercise_files(exercise_number)
    for template_name in exercise_file_names:
        create_from_template_if_not_exist(template_name, file_name)


def get_exercise_files(exercise_number):
    files = [f'./exercises/{exercise_number}/{file}' for file in listdir(f'./exercises/{exercise_number}/')]
    return files


def create_from_template_if_not_exist(template, file_name):
    file_path = get_file_path(template, file_name)
    if not path.exists(file_path):
        with open(template, "r") as file:
            content = file.read()
        with open(file_path, "w") as file:
            file.write(content)


def get_file_path(template, file_name):
    extension = template.split(".")[-1]
    if extension == "html":
        return f"templates/{file_name}.html"
    if extension == "js":
        return f"static/js/{file_name}.js"
    if extension == "css":
        return f"static/style/{file_name}.css"


def get_file_content(template):
    with open(template, "r") as file:
        return file.read()


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
