from data.database import admin_connection, execute_select


@admin_connection
def get_users(connection):
    return execute_select(connection, "select * from users")


@admin_connection
def get_or_create_user(connection, user_name):
    return execute_select(connection,
                          """SELECT * FROM get_or_create_user(%(user_name)s)""",
                          {"user_name": user_name})
