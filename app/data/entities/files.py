from data import database


def get_files_by_project(project_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""select * from files where project_id = {project_id}""")


def get_by_user_id_file_id(file_id, user_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
        select * from files f
        inner join projects p on f.project_id = p.id
        where f.id = {file_id} and p.user_id ={user_id}""")[0]


def update(file_id, content):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection,
                          f"""update files set content=%(content)s where id = {file_id}""",
                          {"content": content})


def is_user_owning_file(file_id, user_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    result = database.execute(connection,
                          f"""select count(*) from files f
                              inner join projects p on f.project_id = p.id
                              where p.user_id = %(user_id)s and f.id = %(user_id)s""",
                          {"file_id": file_id, "user_id": user_id})
    return result > 0
