from data.database import admin_connection, execute_select


@admin_connection
def get_or_create_project(connection, user_id, starter_project_id):
    return execute_select(connection, """SELECT * FROM get_or_create_project({user_id}, {starter_project_id})""")
