from data.entities import projects


from os import path, listdir
from glob import glob


def get_exercises():
    directory_names = [f'{file}' for file in listdir('./exercises/')]
    directory_names.sort()
    return directory_names


def create_user_files(file_name, exercise_number):
    exercise_file_names = get_exercise_files(exercise_number)
    for template_name in exercise_file_names:
        create_from_template_if_not_exist(template_name, file_name, exercise_number)


def get_exercise_files(exercise_number):
    files = [f'./exercises/{exercise_number}/{file}' for file in listdir(f'./exercises/{exercise_number}/')]
    return files


def create_from_template_if_not_exist(template, file_name, exercise_number):
    file_path = get_exercise_path(template, file_name, exercise_number)
    if not path.exists(file_path):
        with open(file_path, "w") as file:
            content = read_file(template)
            file.write(content)


def get_exercise_path(template, user_id, exercise_number):
    extension = template.split(".")[-1]
    file_name = template.split("/")[-1].split(".")[0]
    if is_html_template(file_name, extension):
        return f"templates/exercises/{user_id}-{exercise_number}-{file_name}.{extension}"
    else:
        return f"static/exercises/{user_id}-{exercise_number}-{file_name}.{extension}"


def is_html_template(file_name, extension):
    return extension == "html" and file_name == 'index'


def get_active_exercises():
    projects = [exercise.replace('\\', '/') for exercise in glob("static/exercises/*-code.*")]
    result = [{"user": p.split('-')[0].split('/')[-1], "exerciseNumber": p.split('-')[1]} for p in projects]
    return result


def write_file(user, exercise_number, extension, content):
    file_path = f"./static/exercises/{user}-{exercise_number}-code.{extension}"
    with open(file_path, "w") as file:
        file.write(content)
    return {
        "path": file_path,
        "content": content
    }


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def delete():
    projects.delete_all()
