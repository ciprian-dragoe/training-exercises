from data import database


@database.admin_connection
def get_all(connection):
    return database.execute(connection, """SELECT name, id FROM starter_projects""")
