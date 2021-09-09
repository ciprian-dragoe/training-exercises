import os
import subprocess


def create_python_container(image_name):
    return str(subprocess.check_output(f"docker run -t -d {image_name}", shell=True))[2:-3]


def get_python_execution_result(file_path, kill_container_after_execution=True):
    if kill_container_after_execution:
        container_id = create_python_container(os.environ.get("DOCKER_PYTHON_IMAGE_NAME"))
    else:
        container_id = reusable_container_id
    subprocess.check_output(f"docker cp {file_path} {container_id}:/", shell=True)
    output = str(subprocess.check_output(f'docker exec {container_id} python "/{file_path}"', shell=True))[2:-3]
    if container_id != reusable_container_id:
        subprocess.check_output(f'docker kill {container_id}')

    return output


reusable_container_id = create_python_container(os.environ.get("DOCKER_PYTHON_IMAGE_NAME"))
for i in range(3):
    print(get_python_execution_result("test1.py", False))
for i in range(3):
    print(get_python_execution_result("test1.py"))

subprocess.check_output(f'docker kill {reusable_container_id}', shell=True)
