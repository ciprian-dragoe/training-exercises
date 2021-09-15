import os
from os import path, listdir


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
    file_path = get_file_path(template, file_name, exercise_number)
    if not path.exists(file_path):
        with open(file_path, "w") as file:
            content = read_file(template)
            file.write(content)


def get_file_path(template, file_name, exercise_number):
    extension = template.split(".")[-1]
    if extension == "html":
        return f"templates/exercises/{file_name}-{exercise_number}.{extension}"
    else:
        return f"static/exercises/{file_name}-{exercise_number}.{extension}"


def write_file(user, exercise_number, extension, content):
    file_path = f"static/exercises/{user}-{exercise_number}.{extension}"
    with open(file_path, "w") as file:
        file.write(content)


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def delete_all_exercise_files():
    paths = ['./templates/exercises', './static/exercises']
    for base_path in paths:
        [os.remove(f'{base_path}/{file}') for file in listdir(f'./{base_path}/')]