from data.configuration import CONFIGURATION
from data import database
from services import docker


import subprocess


def manufacture(language_type):
    if language_type in FACTORY:
        return FACTORY[language_type]


def execute_sql(code):
    try:
        if not CONFIGURATION['LANGUAGE_PG_CONTAINER_ID']:
            raise Exception("Admin is not logged in => code execution is disabled")
        connection = database.get_db_connection(database.DbConnection.language_pg)
        query_result = database.execute(connection, code)
        return {"output": query_result}
    except Exception as e:
        return {"error": e.args[0]}


def execute_py(code):
    try:
        sanitized_python_code = generate_sanitized_python_code(code)
        output = docker.get_python_execution_result(sanitized_python_code)
        return {"output": output}
    except subprocess.CalledProcessError as e:
        return {"error": e.output.decode("utf-8")}
    except Exception as e:
        return {"error": e.args[0]}


def generate_sanitized_python_code(code):
    sanitized_code = python_infinite_loop_sanitize_start + code
    return sanitized_code


def execute_html(code):
    return {"output": code}


def execute_js(code):
    return {"output": code}


def execute_css(code):
    return {"output": code}


FACTORY = {
    "sql": execute_sql,
    "css": execute_css,
    "html": execute_html,
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
