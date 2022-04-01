from data import database


def get_all():
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
        SELECT f.name, f.content, p.name as project_name, p.entry_point_starter_file_id
        FROM starter_files f
        inner join starter_projects p on f.starter_project_id = p.id
    """)
