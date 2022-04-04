from data.entities import starter_projects


def get_all():
    result = starter_projects.get_all_project_names()
    return result
