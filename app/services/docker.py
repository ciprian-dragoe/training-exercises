import subprocess
from data.configuration import CONFIGURATION


def create_python_container(image_name):
    return str(subprocess.check_output(f"docker run -t -d {image_name}", shell=True))[2:-3]


def get_python_execution_result(file, language):
    if not CONFIGURATION["DOCKER_CONTAINER_ID"]:
        raise Exception("Admin is not logged in => code execution is disabled")
    handler = DOCKER_EXECUTION_TEMPLATES[language]
    output = handler(file)

    return output


def execute_python(file_path):
    file_name = file_path.split("/")[-1]
    subprocess.check_output(f"docker cp {file_path} {CONFIGURATION['DOCKER_CONTAINER_ID']}:/{file_name}", shell=True)
    output = str(subprocess.check_output(f'docker exec {CONFIGURATION["DOCKER_CONTAINER_ID"]} python /{file_name}', shell=True, stderr=subprocess.STDOUT))[2:-3]

    return output


DOCKER_EXECUTION_TEMPLATES = {
    "py": execute_python
}


def kill_existing_containers():
    if CONFIGURATION["DOCKER_CONTAINER_ID"]:
        try:
            subprocess.check_output(f'docker kill {CONFIGURATION["DOCKER_CONTAINER_ID"]}', shell=True)
        except:
            pass
    CONFIGURATION["DOCKER_CONTAINER_ID"] = None


def initialize():
    # print(f'docker container active: {CONFIGURATION["DOCKER_CONTAINER_ID"]}')
    if not CONFIGURATION["DOCKER_CONTAINER_ID"]:
        CONFIGURATION["DOCKER_CONTAINER_ID"] = create_python_container("training-exercises_language-pg")
