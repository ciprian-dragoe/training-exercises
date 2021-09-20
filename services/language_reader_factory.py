from services import exercises


def manufacture(language_type):
    if language_type in FACTORY:
        return FACTORY[language_type]


def read_sql(user, exercise_number):
    file_path = exercises.get_file_path("code.sql", user, exercise_number)
    file_content = exercises.read_file(file_path)
    return file_content


def read_js(user, exercise_number):
    file_path = exercises.get_file_path("code.js", user, exercise_number)
    file_content = exercises.read_file(file_path)
    return file_content


def read_py(user, exercise_number):
    file_path = exercises.get_file_path("code.py", user, exercise_number)
    file_content = exercises.read_file(file_path)
    return file_content


FACTORY = {
    "sql": read_sql,
    "py": read_py,
    "js": read_js
}
