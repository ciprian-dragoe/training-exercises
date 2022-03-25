import subprocess
from data.configuration import CONFIGURATION


def get_container_id_from(image_name, command_start_container="tail"):
    # return str(subprocess.check_output(f"docker run -td {extra_arguments} {image_name} tail", shell=True))[2:-3]
    try:
        container_id = str(subprocess.check_output(f"docker ps | grep {image_name}", shell=True))[2:-3].split(" ")[0]
        return container_id
    except:
        print(f"THERE WAS A PROBLEM FINDING CONTAINER FROM IMAGE {image_name}")
        container_id = str(subprocess.check_output(f"docker run -td {image_name} {command_start_container}", shell=True))[2:-3]
        return container_id

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


def stop_language_containers():
    if CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        stop_container(CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"])
    if CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"]:
        stop_container(CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"])
    CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"] = None
    CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"] = None


def stop_container(container_id):
    try:
        subprocess.check_output(f'docker container stop {CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]}', shell=True)
    except:
        print(f"THERE WAS A PROBLEM STOPPING CONTAINER WITH ID {container_id}")


def initialize():
    if not CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"] = get_container_id_from("training-exercises_language-py")
    if not CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"]:
        CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"] = get_container_id_from("training-exercises_language-pg", "")
