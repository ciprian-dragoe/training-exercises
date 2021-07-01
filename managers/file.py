from os import path, listdir, walk


def get_max_number_exercises():
    for base, dirs, files in walk('./exercises'):
        return len(dirs)


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


def write_sql_query(user, exercise_number, query):
    file_path = f"static/sql/{user}-{exercise_number}.sql"
    with open(file_path, "w") as file:
        file.write(query)
