from data import database


def get_files(user_id, project_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
    select f.* 
    from files f
    inner join projects p on p.id = f.project_id
    where f.project_id = {project_id} and p.user_id = {user_id}""")


def get(user_id, project_id, file_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
        select f.* from files f
        inner join projects p on f.project_id = p.id
        where f.id = {file_id} and p.user_id ={user_id}  and p.id = {project_id}""")[0]


def update(file_id, content):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection,
                          f"""update files set content=%(content)s where id = {file_id}""",
                          {"content": content},
                           should_return_output=False)


def is_user_owning_file(user_id, file_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    result = database.execute(connection,
                          f"""select count(*) from files f
                              inner join projects p on f.project_id = p.id
                              where p.user_id = {user_id} and f.id = {file_id}""")
    return result[0]['count'] > 0
