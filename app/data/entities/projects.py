from data import database


@database.admin_connection
def get_or_create(connection, user_id, starter_project_id):
    return database.execute(connection, f"""SELECT * FROM get_or_create_project({user_id}, {starter_project_id})""")


@database.admin_connection
def delete(connection, project_id):
    return database.execute(connection, f"""delete from projects where id = {project_id}""", should_return_output=False)


@database.admin_connection
def delete_all(connection):
    return database.execute(connection, f"""delete from projects""", should_return_output=False)


@database.admin_connection
def get(connection, user_id, project_id):
    return database.execute(connection, f"""select * from projects p where p.id = {project_id} and p.user_id = {user_id}""")
