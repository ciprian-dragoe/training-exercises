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
    file = exercises.write_file(user, exercise_number, "py", code)
    try:
        sanitized_python_file_path = generate_sanitized_python_file(file)
        output = docker.get_python_execution_result(sanitized_python_file_path, "py")
        return {"output": output}
    except subprocess.CalledProcessError as e:
        return {"error": e.output.decode("utf-8")}
    except Exception as e:
        return {"error": e.args[0]}


def generate_sanitized_python_file(file):
    sanitized_python_file_path = file["path"][:-file["path"].rfind(".")] + "_sanitized"
    sanitized_code = python_infinite_loop_sanitize_start + file["content"]
    with open(sanitized_python_file_path, "w") as sanitized_file:
        sanitized_file.write(sanitized_code)
    return sanitized_python_file_path


def execute_js(code, user, exercise_number):
    exercises.write_file(user, exercise_number, "js", code)
    return {"output": "True"}


FACTORY = {
    "sql": execute_sql,
    "js": execute_js,
    "py": execute_py
}

python_infinite_loop_sanitize_start = """
import signal
import os
import threading
import time
import sys


def thread_job():
    time.sleep(1)
    print("!!! WARNING ENTERED IN AN INFINITE LOOP !!!")
    
    os.kill(os.getpid(), signal.SIGINT)



fail_safe = threading.Thread(target=thread_job, daemon=True)
fail_safe.start()
"""
