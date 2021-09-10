import subprocess
from data.configuration import CONFIGURATION


def create_python_container(image_name):
    return str(subprocess.check_output(f"docker run -t -d {image_name}", shell=True))[2:-3]


def get_python_execution_result(file_path, kill_container_after_execution=True):
    if not CONFIGURATION["DOCKER-CONTAINER-ID"]:
        raise Exception("admin is not logged in so docker is not enabled")

    if kill_container_after_execution:
        container_id = create_python_container(CONFIGURATION["DOCKER-IMAGE-NAME"])
    else:
        container_id = CONFIGURATION["DOCKER-CONTAINER-ID"]
    subprocess.check_output(f"docker cp {file_path} {container_id}:/", shell=True)
    output = str(subprocess.check_output(f'docker exec {container_id} python "/{file_path}"', shell=True))[2:-3]
    if container_id != CONFIGURATION["DOCKER-CONTAINER-ID"]:
        subprocess.check_output(f'docker kill {container_id}')

    return output


def kill_existing_containers():
    if CONFIGURATION["DOCKER-CONTAINER-ID"]:
        subprocess.check_output(f'docker kill {CONFIGURATION["DOCKER-CONTAINER-ID"]}', shell=True)
    CONFIGURATION["DOCKER-CONTAINER-ID"] = None


def initialize():
    if not CONFIGURATION["DOCKER-CONTAINER-ID"]:
        CONFIGURATION["DOCKER-CONTAINER-ID"] = create_python_container(CONFIGURATION["DOCKER-IMAGE-NAME"])
