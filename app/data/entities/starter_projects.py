from data import database


def get_all():
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, """SELECT name, id FROM starter_projects""")
