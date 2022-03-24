import subprocess
from data.configuration import CONFIGURATION


def launch_container(image_name, extra_arguments=""):
    return str(subprocess.check_output(f"docker run -td {extra_arguments} {image_name} tail", shell=True))[2:-3]


def get_python_execution_result(file, language):
    if not CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        raise Exception("Admin is not logged in => code execution is disabled")
    handler = DOCKER_EXECUTION_TEMPLATES[language]
    output = handler(file)

    return output


def execute_python(file_path):
    file_name = file_path.split("/")[-1]
    subprocess.check_output(f"docker cp {file_path} {CONFIGURATION['LANGUAGE_PY_CONTAINER_ID']}:/{file_name}", shell=True)
    output = str(subprocess.check_output(f'docker exec {CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]} python /{file_name}', shell=True, stderr=subprocess.STDOUT))[2:-3]
    return output


DOCKER_EXECUTION_TEMPLATES = {
    "py": execute_python
}


def kill_existing_containers():
    if CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        subprocess.check_output(f'docker kill {CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]}', shell=True)
    if CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"]:
        subprocess.check_output(f'docker kill {CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"]}', shell=True)
    CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"] = None
    CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"] = None


def initialize():
    if not CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"] = launch_container("training-exercises_language-py")
    if not CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"]:
        CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"] = launch_container("training-exercises_language-pg", f"-p {CONFIGURATION['PRACTICE_PORT']}:5432")
