import subprocess
from data.configuration import CONFIGURATION


def create_python_container(image_name):
    return str(subprocess.check_output(f"docker run -t -d {image_name}", shell=True))[2:-3]


def get_python_execution_result(file, language):
    if not CONFIGURATION["DOCKER-CONTAINER-ID"]:
        raise Exception("Admin is not logged in => code execution is disabled")
    handler = DOCKER_EXECUTION_TEMPLATES[language]
    output = handler(file)

    return output


def execute_python(file):
    file_name = file["path"].split("/")[-1]
    subprocess.check_output(f"docker cp {file['path']} {CONFIGURATION['DOCKER-CONTAINER-ID']}:/{file_name}", shell=True)
    output = str(subprocess.check_output(f'docker exec {CONFIGURATION["DOCKER-CONTAINER-ID"]} python /{file_name}', shell=True, stderr=subprocess.STDOUT))[2:-3]

    return output


DOCKER_EXECUTION_TEMPLATES = {
    "py": execute_python
}




def kill_existing_containers():
    if CONFIGURATION["DOCKER-CONTAINER-ID"]:
        subprocess.check_output(f'docker kill {CONFIGURATION["DOCKER-CONTAINER-ID"]}', shell=True)
    CONFIGURATION["DOCKER-CONTAINER-ID"] = None


def initialize():
    if not CONFIGURATION["DOCKER-CONTAINER-ID"]:
        CONFIGURATION["DOCKER-CONTAINER-ID"] = create_python_container(CONFIGURATION["DOCKER-IMAGE-NAME"])
