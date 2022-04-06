from data.entities import starter_projects


def get_all_by_visibility(visibility = True):
    result = starter_projects.get_all_by_visibility(visibility)
    return result
