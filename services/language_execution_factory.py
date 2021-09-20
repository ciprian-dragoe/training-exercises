import subprocess

from services import exercises, database, docker


def manufacture(language_type):
    if language_type in FACTORY:
        return FACTORY[language_type]


def execute_sql(code, user, exercise_number):
    exercises.write_file(user, exercise_number, "sql", code)
    try:
        query_result = database.execute_select(code)
        return {"output": query_result}
    except Exception as e:
        return {"error": e.args[0]}


def execute_py(code, user, exercise_number):
    file_path = exercises.write_file(user, exercise_number, "py", code)
    try:
        output = docker.get_python_execution_result(file_path, "py")
        return {"output": output}
    except subprocess.CalledProcessError as e:
        return {"error": e.output.decode("utf-8")}
    except Exception as e:
        return {"error": e.args[0]}


def execute_js(code, user, exercise_number):
    exercises.write_file(user, exercise_number, "js", code)
    return {"output": "True"}


FACTORY = {
    "sql": execute_sql,
    "js": execute_js,
    "py": execute_py
}
