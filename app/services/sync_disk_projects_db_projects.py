from data.entities import starter_files


import os


def start():
    disk_projects = get_starter_files_from_disk()
    db_files = starter_files.get_all()

    starter_projects_to_add = []
    for disk_project in disk_projects:
        if is_project_already_in_db(disk_project, db_files):
            db_files_linked_to_project = [file['name'] for file in db_files if file['project_name']]
            starter_files_to_add = get_disk_files_not_in_db(disk_project, db_files_linked_to_project)

            disk_files_linked_to_project = [file for file in disk_project['project_files']]
            starter_files_to_delete = get_db_files_not_on_disk(db_files_linked_to_project, disk_files_linked_to_project)

            starter_files_to_update = get_content_miss_matching_files(db_files_linked_to_project, disk_files_linked_to_project)
        else:
            starter_projects_to_add.append(disk_project)

    db_project_names = set([file['project_name'] for file in db_files])
    disk_project_names = [project['project_name'] for project in disk_projects]
    starter_projects_names_to_delete = [project_name for project_name in db_project_names if project_name not in disk_project_names]


def get_content_miss_matching_files(db_files, disk_files):
    result = []
    for db_file in db_files:
        matching_disk_file = next(file for file in disk_files if disk_files['name'] == db_file['name'])
        if matching_disk_file['content'] != db_file['content']:
            db_file['content'] = matching_disk_file['content']
            result.append(db_file)
    return result


def get_disk_files_not_in_db(disk_project, db_files):
    result = []
    db_file_names = [file['name'] for file in db_files]
    for disk_file in disk_project['project_files']:
        if disk_file['name'] not in db_file_names:
            result.append(disk_file)
    return result


def get_db_files_not_on_disk(db_files, disk_files):
    result = []
    disk_file_names = [file['name'] for file in disk_files]
    for db_file in db_files:
        if db_file['name'] not in disk_file_names:
            result.append(db_file)
    return result


def is_project_already_in_db(disk_project, db_files):
    return any(file for file in db_files if file['project_name'] == disk_project['project_name'])


def get_starter_files_from_disk():
    starter_project_path = './static/starter-projects'
    result = []
    project_names = [f'{project}' for project in os.listdir(starter_project_path)]
    for project_name in project_names:
        project_files_names = [f'{project_file}' for project_file in os.listdir(f'{starter_project_path}/{project_name}/') if 'index.' not in project_file]
        project_files = []
        for file_name in project_files_names:
            with open(f'{starter_project_path}/{project_name}/{file_name}', "r") as file:
                content = file.read()
                project_files.append({"file_name": file_name, "file_content": content})

        result.append({"project_name": project_name, "project_files": project_files})
    return result
