from data import database


def get_or_create(user_id, starter_project_id):
    return database.execute(database.DbConnection.admin,
                            f"""SELECT * FROM get_or_create_project({user_id}, {starter_project_id})""")[0]


def delete(project_id):
    return database.execute(database.DbConnection.admin, f"""delete from projects where id = {project_id}""")


def delete_all():
    return database.execute(database.DbConnection.admin, f"""
        update projects set entry_point_file_id = Null;
        delete from files;
        delete from projects;""")


def get(user_id, project_id):
    return database.execute(database.DbConnection.admin, f"""select * from projects p where p.id = {project_id} and p.user_id = {user_id}""")[0]
