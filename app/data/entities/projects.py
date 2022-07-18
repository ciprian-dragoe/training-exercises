from data import database


def get_or_create(user_id, starter_project_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection,
                            f"""SELECT * FROM get_or_create_project({user_id}, {starter_project_id})""")[0]


def delete(project_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""delete from projects where id = {project_id}""")


def delete_all():
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
        update projects set entry_point_file_id = null;
        delete from files;
        delete from projects;
        delete from users;
""")


def get(user_id, project_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""select * from projects p where p.id = {project_id} and p.user_id = {user_id}""")[0]
