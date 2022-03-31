from data.entities import files


def get_files_by_project(project_id):
    result = files.get_files_by_project(project_id)
    return result


def get(file_id, user_id):
    result = files.get_by_user_id_file_id(file_id, user_id)
    return result
