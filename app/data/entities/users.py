from data import database


def get_users_with_projects():
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, """
    select p.name as prj_name, p.id as prj_id, u.name as user_name, u.id as user_id 
    from projects p
    inner join users u on p.user_id = u.id
    """)


def get_or_create(user_name):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, """SELECT * FROM get_or_create_user(%(user_name)s)""",
                          {"user_name": user_name})[0]
