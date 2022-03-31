from data.entities import projects


def delete_all():
    projects.delete_all()


def get(user_id, project_id):
    projects.get(user_id, project_id)
