from data.configuration import CONFIGURATION
from services.set_timeout import SET_TIMEOUT


import subprocess


def get_container_id_from(image_name, command_start_container="", arguments=""):
    try:
        container_id = str(subprocess.check_output(f"docker ps | grep {image_name}", shell=True))[2:-3].split(" ")[0]
        return container_id
    except:
        print(f"THERE WAS A PROBLEM FINDING CONTAINER OF IMAGE {image_name}")
        container_id = str(subprocess.check_output(f"docker run --rm -td {arguments} {image_name} {command_start_container}", shell=True))[2:-3]
        return container_id


def get_python_execution_result(code):
    if not CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        raise Exception("Admin is not logged in => code execution is disabled")
    escaped_code = code.replace('"', r'\"').replace("'", r"\'")
    instructions = f"/usr/local/bin/docker exec -it {CONFIGURATION['LANGUAGE_PY_CONTAINER_ID']} python -c $'{escaped_code}'"
    output = str(subprocess.check_output(instructions, shell=True, stderr=subprocess.STDOUT))[2:-3]
    return output


def stop():
    if CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        stop_container(CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"])
    if CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"]:
        stop_container(CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"])
    CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"] = None
    CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"] = None


def stop_container(container_id):
    try:
        subprocess.check_output(f'docker container stop {container_id}', shell=True)
    except:
        print(f"THERE WAS A PROBLEM STOPPING CONTAINER WITH ID {container_id}")


def initialize_containers():
    if not CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"]:
        CONFIGURATION["LANGUAGE_PY_CONTAINER_ID"] = get_container_id_from("language_py", "tail")
    if not CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"]:
        CONFIGURATION["LANGUAGE_PG_CONTAINER_ID"] = get_container_id_from("language_pg", "", f"-e POSTGRES_PASSWORD={CONFIGURATION['PRACTICE_PASS']} -e POSTGRES_DB={CONFIGURATION['PRACTICE_DBNAME']} -e POSTGRES_USER={CONFIGURATION['PRACTICE_USER']} --name language_pg --network {CONFIGURATION['NETWORK_NAME']}")


def start():
    initialize_containers()
    SET_TIMEOUT.clear()
    SET_TIMEOUT.run(stop, int(CONFIGURATION["DOCKER_KILL_TIMEOUT_SECONDS"]))
