from data.entities import starter_files, starter_projects


import os


def start():
    disk_projects = get_starter_files_from_disk()
    db_projects = starter_projects.get_all_projects_with_files()
    imports = get_db_projects_to_update(disk_projects, db_projects)
    for project in imports['starter_projects_add']:
        new_project = starter_projects.create(project)
        for file in project['files']:
            file['starter_project_id'] = new_project['id']
            new_file = starter_files.create(file)
            if 'main.' in new_file['name']:
                starter_projects.update_starter_file(new_project['id'], new_file['id'])

    for name in imports['starter_project_names_delete']:
        # todo: ce se intampla cu fisierele ramase de la acel proiect
        starter_projects.delete_by_name(name)

    for file in imports['starter_files_add']:
        new_file = starter_files.create(file)
        if 'main.' in new_file['name']:
            starter_projects.update_starter_file(new_file['starter_project_id'], new_file['id'])

    for file in imports['starter_files_delete']:
        starter_files.delete(file['file_id'])

    for file in imports['starter_files_update']:
        starter_files.update_content(file['file_id'], file['content'])
    print(imports)


def get_db_projects_to_update(disk_projects, db_projects):
    result = {
        "starter_projects_add": [],
        "starter_project_names_delete": [],
        "starter_files_add": [],
        "starter_files_delete": [],
        "starter_files_update": [],
    }
    for disk_project in disk_projects:
        if is_project_already_in_db(disk_project, db_projects):
            db_files_linked_to_project = [project for project in db_projects if project['project_name'] == disk_project['name']]
            result['starter_files_add'] += get_disk_files_not_in_db(disk_project, db_files_linked_to_project)

            disk_files_linked_to_project = [file for file in disk_project['files']]
            result['starter_files_delete'] += get_db_files_not_on_disk(db_files_linked_to_project,
                                                                         disk_files_linked_to_project)

            result['starter_files_update'] += get_content_miss_matching_files(db_files_linked_to_project,
                                                                      disk_files_linked_to_project)
        else:
            result['starter_projects_add'].append(disk_project)

    db_project_names = set([project['project_name'] for project in db_projects])
    disk_project_names = [project['name'] for project in disk_projects]
    result['starter_project_names_delete'] = [project_name for project_name in db_project_names if
                                        project_name not in disk_project_names]

    return result


def get_content_miss_matching_files(db_files, disk_files):
    result = []
    for db_file in db_files:
        matching_disk_file = next((file for file in disk_files if file['name'] == db_file['file_name']), None)
        if matching_disk_file and matching_disk_file['content'] != db_file['file_content']:
            db_file['content'] = matching_disk_file['content']
            result.append(db_file)
    return result


def get_disk_files_not_in_db(disk_project, db_files):
    result = []
    db_file_names = [file['file_name'] for file in db_files]
    for disk_file in disk_project['files']:
        if disk_file['name'] not in db_file_names:
            disk_file['starter_project_id'] = db_files[0]['project_id']
            result.append(disk_file)
    return result


def get_db_files_not_on_disk(db_files, disk_files):
    result = []
    disk_file_names = [file['name'] for file in disk_files]
    for db_file in db_files:
        if db_file['file_id'] and db_file['file_name'] not in disk_file_names:
            result.append(db_file)
    return result


def is_project_already_in_db(disk_project, db_files):
    return any(file for file in db_files if file['project_name'] == disk_project['name'])


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
                project_files.append({"name": file_name, "content": content})

        result.append({"name": project_name, "files": project_files})
    return result
