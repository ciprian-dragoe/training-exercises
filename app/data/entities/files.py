from data import database


@database.admin_connection
def get_files_by_project(connection, project_id):
    return database.execute(connection, f"""select * from files where project_id = {project_id}""")


@database.admin_connection
def get_by_user_id_file_id(connection, file_id, user_id):
    return database.execute(connection, f"""
        select * from files f
        inner join projects p on p.user_id = {user_id}
        where id = {file_id}""")


@database.admin_connection
def update(connection, file_id, content):
    return database.execute(connection,
                          f"""update files set content=%(content)s where id = {file_id}""",
                          {"content": content})


@database.admin_connection
def is_user_owning_file(connection, file_id, user_id):
    result = database.execute(connection,
                          f"""select count(*) from files f
                              inner join projects p on f.project_id = p.id
                              where p.user_id = %(user_id)s and f.id = %(user_id)s""",
                          {"file_id": file_id, "user_id": user_id})
    return result > 0
