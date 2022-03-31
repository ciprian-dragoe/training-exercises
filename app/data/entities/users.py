from data import database


@database.admin_connection
def get_users_with_projects(connection):
    return database.execute(connection, """
    select * from users u
    inner join projects p on p.user_id = u.id
    """)


@database.admin_connection
def get_or_create(connection, user_name):
    return database.execute(connection,
                          """SELECT * FROM get_or_create_user(%(user_name)s)""",
                          {"user_name": user_name})
