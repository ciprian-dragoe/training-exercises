from data.entities import projects


import os


def delete_all():
    projects.delete_all()


def get(user_id, project_id):
    return projects.get(user_id, project_id)


def get_project_starter_template(user_id, project_id):
    template = get(user_id, project_id)
    template_name = template['name']
    with open(f'{os.getcwd()}/static/starter-projects/{template_name}/index.html') as file:
        template_content = file.read()
        return template_content, template_name


def create_from_starter_template(user_id, starter_project_id):
    return projects.get_or_create(user_id, starter_project_id)
