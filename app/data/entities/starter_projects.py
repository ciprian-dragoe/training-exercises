from data.database import admin_connection, execute_select


@admin_connection
def get_starter_projects(connection):
    return execute_select(connection, """SELECT name, id FROM starter_projects""")
