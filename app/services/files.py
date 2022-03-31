from data.entities import files


def get_files(user_id, project_id):
    result = files.get_files(user_id, project_id)
    return result


def get(user_id, project_id, file_id):
    result = files.get(user_id, project_id, file_id)
    return result
